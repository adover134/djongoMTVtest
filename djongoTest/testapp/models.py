from djongo import models


class User(models.Model):
    u_id = models.TextField(primary_key=True, default="")
    u_name = models.TextField(default="홍길동")
    u_email = models.EmailField(default="aaaaa@aaa.com")
    inactivated_date = models.DateField(null=True)

    class Meta:
        db_table = "user"


class Manager(models.Model):
    m_id = models.TextField(primary_key=True, default="")
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="u_id")
    m_tel = models.TextField(default="010-0101-1010")

    class Meta:
        db_table = "manager"
