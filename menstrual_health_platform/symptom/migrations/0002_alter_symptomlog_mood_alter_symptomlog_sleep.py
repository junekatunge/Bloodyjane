# Generated by Django 4.2.15 on 2024-08-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("symptom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="symptomlog",
            name="mood",
            field=models.CharField(
                choices=[
                    ("Excellent", "Excellent"),
                    ("Good", "Good"),
                    ("Neutral", "Neutral"),
                    ("Bad", "Bad"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="symptomlog",
            name="sleep",
            field=models.CharField(
                choices=[
                    ("Excellent", "Excellent"),
                    ("Good", "Good"),
                    ("Fair", "Fair"),
                    ("Poor", "Poor"),
                    ("Very Poor", "Very Poor"),
                ],
                max_length=20,
            ),
        ),
    ]
