from project import db
from project.models import User

# create table
db.create_all()

# insert data
db.session.add(User("admin", "admin@iws.com", "admin"))
db.session.add(User("stevejobs", "stevejobs@iws.com", "5october2011"))
db.session.add(User("elonmusk", "elonmusk@iws.com", "28june"))


# commit the changes
db.session.commit()
