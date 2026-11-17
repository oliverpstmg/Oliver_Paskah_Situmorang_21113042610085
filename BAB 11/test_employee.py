

from employee import Employee

def test_give_default_raise():
    """Menguji apakah kenaikan gaji default ($5,000) berfungsi dengan benar."""
    employee = Employee("Budi", "Santoso", 60000)
    employee.give_raise()
    assert employee.annual_salary == 65000

def test_give_custom_raise():
    """Menguji apakah kenaikan gaji kustom berfungsi dengan benar."""
    employee = Employee("Siti", "Rahma", 70000)
    employee.give_raise(10000)
    assert employee.annual_salary == 80000