from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    u_name = models.TextField(default="홍길동")
    u_email = models.EmailField(unique=True, default="aaaaa@aaa.com")
    inactivated_date = models.DateField(null=True)
    u_access_token = models.TextField(unique=True, default="")

    class Meta:
        db_table = "user"

    def __str__(self):
        return ""+self.u_name+", "+self.u_email


class Manager(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user", db_column="u_id")
    m_tel = models.TextField(default="010-0101-1010")

    class Meta:
        db_table = "manager"
