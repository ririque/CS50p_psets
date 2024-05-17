from seasons import check_date
import pytest

def main():
    test_check_date()

def test_check_date():
    assert check_date(2024, 4, 26) == "One thousand, four hundred forty"

if __name__ == "__main__":
    main()
