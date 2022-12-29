from django.db import migrations


def describe_items(apps, schema_editor):
    Item = apps.get_model('post', 'Item')
    Item.objects.create(name='Reticule', price=25.75, disc_price=0,
                        desc='Black laquered reticule made of textures leather', img='bag.jpg', category='des')
    Item.objects.create(name='Cargo trousers', price=30.25, disc_price=0,
                        desc='Sand colored cargo trousers with big pockets', img='cargo.jpg', category='des')
    Item.objects.create(name='Fur coat', price=40.45, disc_price=0,
                        desc='Soft and warm quilted fur coat made of natural rabbit fur', img='coat_fur.jpg',
                        category='des')
    Item.objects.create(name='Sheepskin coat', price=34.60, disc_price=0, desc='Natural warm sheepskin coat',
                        img='coat.jpg', category='des')
    Item.objects.create(name='Jacket', price=0, disc_price=0, desc='Designed shortened deep-blue jacket',
                        img='jacket.jpg', category='gra')
    Item.objects.create(name='Grey skirt', price=32.50, disc_price=22.50, desc='Perfect grey wool skirt',
                        img='skirt.jpg', category='poi')
    Item.objects.create(name='Grey Trousers', price=42.10, disc_price=32.10,
                        desc='Wool grey trousers with glencheck print', img='trousers_grey.jpg', category='poi')
    Item.objects.create(name='Green waistcoat', price=0, disc_price=0, desc='Wool and acryl green waistcoat',
                        img='waistcoat_green.jpg', category='gra')
    Item.objects.create(name='Red waistcoat', price=63.20, disc_price=53.20,
                        desc='Silk red waistcoat with golden buttons', img='waistcoat_red.jpg', category='poi')
    Item.objects.create(name='Home costume', price=91.30, disc_price=81.30, desc='Home wool trousers and cardigan',
                        img='home_costume.jpg', category='poi')


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [migrations.RunPython(describe_items)]
