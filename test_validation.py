import unittest

from scholarship_portal import (
    ScholarshipValidator,
    ScholarshipValidationError,
    IDFormatError,
    EmailDomainError,
    GWARangeError,
)


class TestScholarshipValidator(unittest.TestCase):

    def test_valid_name(self):
        result = ScholarshipValidator.validate_name("Maria Clara Santos")
        self.assertEqual(result, "Maria Clara Santos")

    def test_empty_name(self):
        with self.assertRaises(ScholarshipValidationError):
            ScholarshipValidator.validate_name("")

    def test_invalid_name(self):
        with self.assertRaises(ScholarshipValidationError):
            ScholarshipValidator.validate_name("Maria123")

    def test_valid_student_id(self):
        result = ScholarshipValidator.validate_student_id("2024-0123")
        self.assertEqual(result, "2024-0123")

    def test_invalid_student_id(self):
        with self.assertRaises(IDFormatError):
            ScholarshipValidator.validate_student_id("2024-123")

    def test_valid_email(self):
        result = ScholarshipValidator.validate_email(
            "maria.santos@cspc.edu.ph"
        )
        self.assertEqual(result, "maria.santos@cspc.edu.ph")

    def test_non_cspc_email(self):
        with self.assertRaises(EmailDomainError):
            ScholarshipValidator.validate_email(
                "maria.santos@gmail.com"
            )

    def test_valid_phone(self):
        result = ScholarshipValidator.validate_phone("09181234567")
        self.assertEqual(result, "09181234567")

    def test_valid_international_phone(self):
        result = ScholarshipValidator.validate_phone("+639181234567")
        self.assertEqual(result, "09181234567")

    def test_invalid_phone(self):
        with self.assertRaises(ScholarshipValidationError):
            ScholarshipValidator.validate_phone("123456789")

    def test_valid_gwa(self):
        result = ScholarshipValidator.validate_gwa("1.45")
        self.assertEqual(result, 1.45)

    def test_nonnumeric_gwa(self):
        with self.assertRaises(GWARangeError):
            ScholarshipValidator.validate_gwa("uno")

    def test_out_of_range_gwa(self):
        with self.assertRaises(GWARangeError):
            ScholarshipValidator.validate_gwa("6.00")

    def test_gwa_boundary(self):
        result = ScholarshipValidator.validate_gwa("1.00")
        self.assertEqual(result, 1.00)


if __name__ == "__main__":
    unittest.main()
