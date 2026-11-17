# File: test_employee.py

python -m pytestimport pytest
from employee import Employee

@pytest.fixture
def general_employee():
    """Membuat objek Employee yang dapat digunakan kembali oleh fungsi tes."""
    employee = Employee("Budi", "Santoso", 60000)
    return employee

def test_give_default_raise(general_employee):
    """Menguji kenaikan gaji default menggunakan fixture."""
    general_employee.give_raise()
    assert general_employee.annual_salary == 65000

def test_give_custom_raise(general_employee):
    """Menguji kenaikan gaji kustom menggunakan fixture."""
    general_employee.give_raise(10000)
    assert general_employee.annual_salary == 70000  # Perhatikan: fixture memberikan instance baru yang segar untuk setiap tes