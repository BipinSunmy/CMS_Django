# Generated by Django 5.1.5 on 2025-01-29 05:40

import APP.models
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("a_id", models.AutoField(primary_key=True, serialize=False)),
                ("token", models.IntegerField(blank=True)),
                ("DoA", models.DateField(validators=[APP.models.past_day])),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="BloodGroup",
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
                ("blood", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Lab",
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
                ("test", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Medicine",
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
                ("medicine", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Qualifications",
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
                ("name", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Specialization",
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
                ("specialization", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Time",
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
                ("Timings", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "doc_id",
                    models.CharField(
                        max_length=25, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("f_name", models.CharField(max_length=25)),
                ("l_name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("DoB", models.DateField(validators=[APP.models.doctor_age])),
                ("address", models.CharField(default="No", max_length=100)),
                ("fee", models.IntegerField()),
                ("phone", models.CharField(max_length=10)),
                ("Available", models.BooleanField(default=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("DoJ", models.DateField(default=datetime.date.today)),
                ("salary", models.IntegerField()),
                (
                    "l_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("Qualification", models.ManyToManyField(to="APP.qualifications")),
                (
                    "specialization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="APP.specialization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Billing",
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
                    "a_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="APP.appointment",
                    ),
                ),
                (
                    "d_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.doctor"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="d_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="APP.doctor"
            ),
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=25)),
                ("DoB", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
                (
                    "bg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.bloodgroup"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="p_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="APP.patient"
            ),
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("types", models.CharField(max_length=25)),
                (
                    "b_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.billing"
                    ),
                ),
                (
                    "p_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.patient"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prescrible",
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
                ("notes", models.CharField(max_length=150)),
                (
                    "d_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.doctor"
                    ),
                ),
                ("medicine", models.ManyToManyField(default=None, to="APP.medicine")),
                (
                    "p_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="APP.patient"
                    ),
                ),
                ("test", models.ManyToManyField(default=None, to="APP.lab")),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("f_name", models.CharField(max_length=25)),
                ("l_name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.CharField(default="No", max_length=100)),
                ("DoB", models.DateField(validators=[APP.models.staff_age])),
                ("salary", models.IntegerField()),
                ("DoJ", models.DateField(default=datetime.date.today)),
                ("isActive", models.BooleanField(default=True)),
                ("Qualification", models.ManyToManyField(to="APP.qualifications")),
                (
                    "l_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="time",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="APP.time"
            ),
        ),
    ]
