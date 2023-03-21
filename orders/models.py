from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    table_number = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('added', 'Added'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('canceled', 'Canceled'),
        ('paid', 'Paid')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='added')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return 'Table ' + str(self.table_number) + ' - ' + str(self.price)

