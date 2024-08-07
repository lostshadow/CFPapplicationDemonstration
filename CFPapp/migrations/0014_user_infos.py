# Generated by Django 3.2.18 on 2024-03-13 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CFPapp', '0013_auto_20240312_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('anciennete_annee', models.IntegerField()),
                ('anciennete_mois', models.IntegerField()),
                ('fonction', models.CharField(choices=[('GRM', 'CFP au Greta Rouen Maritime'), ('GPN', 'CFP au Greta Portes Normandes'), ('GCN', 'CFP au Greta Côtes Normandes'), ('DDAT', 'DDAT'), ('DRFPIC', 'CFP DRFPIC'), ('IFPRA', 'CFP IFPRA')], default='GRM', max_length=20)),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
