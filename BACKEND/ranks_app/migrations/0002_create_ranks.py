from django.db import migrations


def create_ranks(apps, schema_editor):
    Rank = apps.get_model('ranks_app', 'Rank')

    ranks = [
        ('Private', 'PV1', 0, 1, False),
        ('Private Second Class', 'PV2', 100, 2, False),
        ('Private First Class', 'PFC', 250, 3, False),
        ('Specialist', 'SPC', 500, 4, False),
        ('Corporal', 'CPL', 900, 5, False),
        ('Sergeant', 'SGT', 1500, 6, True),
        ('Staff Sergeant', 'SSG', 2500, 7, True),
        ('Sergeant First Class', 'SFC', 4000, 8, True),
        ('Master Sergeant', 'MSG', 6000, 9, True),
        ('First Sergeant', '1SG', 8500, 10, True),
        ('Sergeant Major', 'SGM', 11500, 11, True),
        ('Command Sergeant Major', 'CSM', 15000, 12, True),
        ('Sergeant Major of the Army', 'SMA', 20000, 13, True),
    ]

    for name, abbreviation, min_xp, order, requires_approval in ranks:
        Rank.objects.create(
            name=name,
            abbreviation=abbreviation,
            min_xp=min_xp,
            category='ENLISTED',
            order=order,
            requires_approval=requires_approval,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('ranks_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_ranks),
    ]