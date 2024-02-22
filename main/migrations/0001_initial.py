# Generated by Django 5.0.2 on 2024-02-21 21:51

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_category', models.CharField(help_text='(Мясные, Молочные, Хлебобулочные и т.д.)', max_length=75, verbose_name='Наименование категории')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='FatAcids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название Жирнокислоты')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
            ],
            options={
                'verbose_name': ' -- (Виды Жирнокислоты) -- ',
            },
        ),
        migrations.CreateModel(
            name='FatAcidsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип жирнокислоты')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50, verbose_name='Регион')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Science Staff')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_name', models.CharField(max_length=75, verbose_name='Наименование продукта')),
                ('date_analis', models.DateField(default=django.utils.timezone.now, verbose_name='Дата исследования')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.categories', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': ' -- Наименование продукта -- ',
            },
        ),
        migrations.CreateModel(
            name='MineralComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ca', models.FloatField(default=0, verbose_name='Ca (Кальций)')),
                ('Na', models.FloatField(default=0, verbose_name='Na (Натрий)')),
                ('K', models.FloatField(default=0, verbose_name='K (Калий)')),
                ('P', models.FloatField(default=0, verbose_name='P (Фосфор)')),
                ('Mn', models.FloatField(default=0, verbose_name='Mn (Марганец)')),
                ('Zn', models.FloatField(default=0, verbose_name='Zn (Цинк)')),
                ('Se', models.FloatField(default=0, verbose_name='Se (Скандий)')),
                ('Cu', models.FloatField(default=0, verbose_name='Cu (Медь)')),
                ('Fe', models.FloatField(default=0, verbose_name='Fe (Железо)')),
                ('I', models.FloatField(default=0, verbose_name='I (Йод)')),
                ('B', models.FloatField(default=0, verbose_name='B (Бор)')),
                ('Li', models.FloatField(default=0, verbose_name='Li (Литий)')),
                ('Al', models.FloatField(default=0, verbose_name='Al (Алюминий)')),
                ('Mg', models.FloatField(default=0, verbose_name='Mg (Магний)')),
                ('V', models.FloatField(default=0, verbose_name='V (Ванадий)')),
                ('Ni', models.FloatField(default=0, verbose_name='Ni (Нитрий)')),
                ('Co', models.FloatField(default=0, verbose_name='Co (Ковальт)')),
                ('Cr', models.FloatField(default=0, verbose_name='Cr (Хром)')),
                ('Sn', models.FloatField(default=0, verbose_name='Sn (Олово)')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Минеральный состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='FatAcidCompositionOfMeal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField(verbose_name='Содержание')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
                ('fat_acid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fatacids', verbose_name='Вид жирнокислоты')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fatacidstype', verbose_name='Тип жирных кислоты')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Жирнокислотный Состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluable_solids', models.FloatField(default=0, verbose_name='Массовая доля растворимых сухих веществ, %')),
                ('ascorbic_acids', models.FloatField(default=0, verbose_name='Массовая доля аскорбиновой кислоты, г/дм3')),
                ('ash_content', models.FloatField(default=0, verbose_name='Зольность, %')),
                ('moisture', models.FloatField(default=0, verbose_name='Массовая доля влаги, %')),
                ('protein', models.FloatField(default=0, verbose_name='Массовая доля белка, %')),
                ('fat', models.FloatField(default=0, verbose_name='Массовая доля жира, %')),
                ('carbohydrates', models.FloatField(default=0, verbose_name='Массовая доля углевода, %')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Химический состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='AminoAcidComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asparing', models.FloatField(default=0, verbose_name='Аспарагиновая кислота')),
                ('glutamin', models.FloatField(default=0, verbose_name='Глутаминовая кислота')),
                ('serin', models.FloatField(default=0, verbose_name='Серин')),
                ('gistidin', models.FloatField(default=0, verbose_name='Гистидин')),
                ('glitsin', models.FloatField(default=0, verbose_name='Глицин')),
                ('treonin', models.FloatField(default=0, verbose_name='Треонин')),
                ('arginin', models.FloatField(default=0, verbose_name='Аргинин')),
                ('alanin', models.FloatField(default=0, verbose_name='Аланин')),
                ('tirosin', models.FloatField(default=0, verbose_name='Тирозин')),
                ('tsistein', models.FloatField(default=0, verbose_name='Цистеин')),
                ('valin', models.FloatField(default=0, verbose_name='Валин')),
                ('metionin', models.FloatField(default=0, verbose_name='Метионин')),
                ('triptofan', models.FloatField(default=0, verbose_name='Триптофан')),
                ('fenilalalin', models.FloatField(default=0, verbose_name='Фенилаланин')),
                ('izoleitsin', models.FloatField(default=0, verbose_name='Изолейцин')),
                ('leitsin', models.FloatField(default=0, verbose_name='Лейцин')),
                ('lisin', models.FloatField(default=0, verbose_name='Лизин')),
                ('prolin', models.FloatField(default=0, verbose_name='Пролин')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
            options={
                'verbose_name': ' -- (Аминокислотный Состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='Recips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=85, verbose_name='Наименование рецептуры')),
                ('cost_price_100gramm', models.FloatField(default=0, verbose_name='Себестоимость')),
                ('cost_price_1kg', models.FloatField(default=0, verbose_name='Себестоимость')),
                ('date_analis', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата проектирования')),
                ('language', models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ('Кыргызча', 'Кыргызча')], default='Русский', max_length=50, verbose_name='Язык')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass_fraction', models.FloatField(default=0, verbose_name='Массовая доля в рецепте')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
                ('recip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recips')),
            ],
        ),
        migrations.CreateModel(
            name='ChemicalsRecip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein', models.FloatField(default=0, verbose_name='Массовая доля белка, %')),
                ('fat', models.FloatField(default=0, verbose_name='Массовая доля жира, %')),
                ('carbohydrates', models.FloatField(default=0, verbose_name='Массовая доля углевода, %')),
                ('kkal', models.FloatField(default=0, verbose_name='ккал')),
                ('kJ', models.FloatField(default=0, verbose_name='кДж')),
                ('recip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recips')),
            ],
            options={
                'verbose_name': ' -- (Химический состав) -- ',
            },
        ),
        migrations.CreateModel(
            name='AminoAcidCompositionRecip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izoleitsin', models.FloatField(default=0, verbose_name='Изолейцин')),
                ('leitsin', models.FloatField(default=0, verbose_name='Лейцин')),
                ('lisin', models.FloatField(default=0, verbose_name='Лизин')),
                ('valin', models.FloatField(default=0, verbose_name='Валин')),
                ('metilcistein', models.FloatField(default=0, verbose_name='Метилцистеин')),
                ('feniltirosin', models.FloatField(default=0, verbose_name='Фенилтиросин')),
                ('triptofan', models.FloatField(default=0, verbose_name='Триптофан')),
                ('treon', models.FloatField(default=0, verbose_name='Треон')),
                ('izoleitsin1', models.FloatField(default=0, verbose_name='Изолейцин C, %')),
                ('leitsin1', models.FloatField(default=0, verbose_name='Лейцин C, %')),
                ('lisin1', models.FloatField(default=0, verbose_name='Лизин C, %')),
                ('valin1', models.FloatField(default=0, verbose_name='Валин C, %')),
                ('metilcistein1', models.FloatField(default=0, verbose_name='Метилцистеин C, %')),
                ('feniltirosin1', models.FloatField(default=0, verbose_name='Фенилтиросин C, %')),
                ('triptofan1', models.FloatField(default=0, verbose_name='Триптофан C, %')),
                ('treon1', models.FloatField(default=0, verbose_name='Треон C, %')),
                ('izoleitsin_a', models.FloatField(default=0, verbose_name='Изолейцин a, %')),
                ('leitsin_a', models.FloatField(default=0, verbose_name='Лейцин a, %')),
                ('lisin_a', models.FloatField(default=0, verbose_name='Лизин a, %')),
                ('valin_a', models.FloatField(default=0, verbose_name='Валин a, %')),
                ('metilcistein_a', models.FloatField(default=0, verbose_name='Метилцистеин a, %')),
                ('feniltirosin_a', models.FloatField(default=0, verbose_name='Фенилтиросин a, %')),
                ('triptofan_a', models.FloatField(default=0, verbose_name='Триптофан a, %')),
                ('treon_a', models.FloatField(default=0, verbose_name='Треон a, %')),
                ('c_min', models.FloatField(default=0, verbose_name='Cmin')),
                ('recip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recips')),
            ],
            options={
                'verbose_name': ' -- (Аминокислотный Состав) -- ',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='regions_category', to='main.regions'),
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
