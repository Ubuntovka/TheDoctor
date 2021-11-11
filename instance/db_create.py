import sys
import os

print('Creating database tables for TheDoctor app...')

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))

# Create the database tables, add some initial data, and commit to the database
from app import db
from app.models import Doctor, Article

# Drop all of the existing database tables
db.drop_all()

# Create the database and the database table
db.create_all()

# Insert articles data
at1 = Article(title='Spinach in a healthy diet', intro='The benefits of leafy greens',
              text='Spinach is a green vegetable. It is used in medicine, cosmetology and cooking. In terms of folic'
                   ' acid content, the plant is the leader among greens. “Spinach is rich in fiber and vitamin K,'
                   ' which are synthesized in the intestines.The plant also contains vitamins C, B2, B6, B9, a lot '
                   'of Omega-3 of plant origin and very important microelements for humans: magnesium, zinc, cuprum,'
                   ' selenium. An important factor is the content of lutein, which is useful for people if they are '
                   'diagnosed with vision problems, ”says Taras Bulanov, medical director of the Medibor clinic. Among'
                   ' the varieties of this culture, spinach Uteusha (Uteusha Rumeks), or, as it is also called, spinach'
                   ' sorrel, is distinguished. When buying spinach, pay special attention to the leaves. They should'
                   ' not have dark spots - this is a sign of a stale plant. As spinach withers, it becomes toxic '
                   'to the body.')
at2 = Article(title='May is a period of high tick activity!', intro='Tick removal and consultation with a doctor.',
              text='What could be better than fresh juicy green grass? It is so nice to stay with your family in a '
                   'sun-drenched meadow in the middle of a natural grass carpet. But a small insect can spoil the rest,'
                   ' which sometimes becomes the cause of prolonged malaise. These are ticks, which have the highest'
                   ' activity in April-May and August-September.Why is a tick bite dangerous?\nThe insect can '
                   'carry pathogens of such diseases:\n1) viral encephalitis;\n2) Marseilles fever,\n3) '
                   'borreliosis or Lyme disease.\nEach of the diseases is manifested by an increase in body '
                   'temperature, weakness, nausea, redness and swelling at the site of the bite.\nHow to reduce the '
                   'risk of being bitten?\n1) Give preference to clothing with long sleeves and cuffs, even if it '
                   'is very hot;\n2) Thoroughly examine yourself at home on a white background - best in the bath;\n3) '
                   'Wear a hat;\n4) Tuck trousers into socks and wear closed shoes;\n5) Be sure to wash your clothes '
                   'immediately after walking;\n5) Choose clothes with a high collar that covers the neck.\n6) Most '
                   'often, mites stick to where the skin is thinnest: the armpits, groin, under the knee, scalp.\nWhat'
                   ' to do in case of a tick bite:\nThe main thing when finding a tick is not to panic! After all,'
                   ' the desire to remove the insect as quickly as possible can lead to exaggeration of efforts, and '
                   'the tick will be damaged when removed. In such cases, the proboscis remains in the skin and'
                   ' suppuration occurs at the site of the bite.\nThe ideal option is to seek medical attention. '
                   'After all, the tick proboscis has a specific spiral structure and the usual mechanical removal '
                   '(just pull it out) increases the chances of leaving the proboscis in the body with the following '
                   'complications.\nTherefore, the advantage of qualified medical care is sterility during the '
                   'procedure. On the recommendation of a doctor, 3-5 days after the bite, it is recommended to '
                   'donate blood for an Ig M analysis to Borelia Burdhoferi.')
db.session.add(at1)
db.session.add(at2)

# Commit the changes for the users
db.session.commit()

# Insert doctors data
d1 = Doctor(fio='Stepanov Nikolay Andreevich', specialty='pediatrician', position='doctor', experience=5,
            photo=b'photos_of_doctors/dr1.jpg', working_time='10:00-18:00')
d2 = Doctor(fio='Lipnitsky Alexey Nikolaevich', specialty='ophthalmologist', position='doctor', experience=12,
            photo=b'photos_of_doctors/dr2.jpg', working_time='10:00-18:00')
d3 = Doctor(fio='Soldatenko Vasily Anatolievich', specialty='gynecologist', position='medical director', experience=8,
            photo=b'photos_of_doctors/dr3.jpg', working_time='10:00-18:00')
d4 = Doctor(fio='Mikhailenko Alexander Artemovich', specialty='gynecologist', position='doctor', experience=2,
            photo=b'photos_of_doctors/dr4.jpg', working_time='10:00-18:00')
d5 = Doctor(fio='Fofanov Elizar Sviridovich', specialty='gastroenterologist', position='doctor', experience=10,
            photo=b'photos_of_doctors/dr5.jpg', working_time='10:00-18:00')

db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(d4)
db.session.add(d5)

# Commit the changes for the recipes
db.session.commit()

print('...done!')
