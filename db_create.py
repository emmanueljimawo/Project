from project import db
from datetime import date
from project.models import User
from project.models import FeatureRequest


# create table
db.create_all()

# insert data
db.session.add(User("admin", "admin@iws.com", "admin"))
db.session.add(User("stevejobs", "stevejobs@iws.com", "5october2011"))
db.session.add(User("elonmusk", "elonmusk@iws.com", "28june"))

db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client B", 1, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client C", 2, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client A", 3, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client A", 4, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client B", 5, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client B", 6, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client C", 1, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client C", 1, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client B", 2, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client A", 2, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client C", 3, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client C", 3, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client B", 1, date.today(), "Billing", "1"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client A", 2, date.today(), "Billing", "2"))
db.session.add(FeatureRequest("Test request", "This is a test request",
                         "Client A", 1, date.today(), "Billing", "2"))


# commit the changes
db.session.commit()


# # drop table
# db.drop_all()
