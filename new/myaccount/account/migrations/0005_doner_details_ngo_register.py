# Generated by Django 4.1.5 on 2023-01-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_remove_user_address_remove_user_city_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doner_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dd_username",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="User Name"
                    ),
                ),
                ("dd_email", models.EmailField(max_length=100, verbose_name="Email")),
                ("phone_number", models.IntegerField()),
                (
                    "donation_from",
                    models.CharField(
                        choices=[
                            ("1", "Restaurent"),
                            ("2", "Mess"),
                            ("3", "Hotel"),
                            ("4", "Hostel"),
                            ("5", "Events"),
                            ("6", "Donation"),
                            ("7", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("pincode", models.CharField(max_length=10, null=True)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="NGO_Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "org_name",
                    models.CharField(max_length=100, verbose_name="Organiser Name"),
                ),
                ("register_id", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("pincode", models.CharField(max_length=6)),
                ("contact", models.IntegerField()),
                ("pwd", models.CharField(max_length=50, verbose_name="password")),
                (
                    "con_pwd",
                    models.CharField(max_length=50, verbose_name=" confirm password"),
                ),
            ],
        ),
    ]
