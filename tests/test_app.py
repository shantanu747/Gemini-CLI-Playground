import pytest
from app import app
from database import db_session, init_db, Base, engine
from models import Bug
import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)


def test_update_status_to_in_progress(client):
    # Create a new bug
    new_bug = Bug(title="Test Bug", status="To Do")
    db_session.add(new_bug)
    db_session.commit()
    bug_id = new_bug.id

    # Update the status
    client.post(f'/update_status/{bug_id}', data={'status': 'In Progress'})

    # Verify the status is updated
    updated_bug = db_session.get(Bug, bug_id)
    assert updated_bug.status == 'In Progress'
    assert updated_bug.completion_date is None

def test_update_status_to_done(client):
    # Create a new bug
    new_bug = Bug(title="Test Bug", status="To Do")
    db_session.add(new_bug)
    db_session.commit()
    bug_id = new_bug.id

    # Update the status
    client.post(f'/update_status/{bug_id}', data={'status': 'Done'})

    # Verify the status and completion date
    updated_bug = db_session.get(Bug, bug_id)
    assert updated_bug.status == 'Done'
    assert updated_bug.completion_date is not None

def test_update_status_from_done(client):
    # Create a new bug that is already 'Done'
    completion_date = datetime.datetime.now(datetime.UTC)
    new_bug = Bug(title="Test Bug", status="Done", completion_date=completion_date)
    db_session.add(new_bug)
    db_session.commit()
    bug_id = new_bug.id

    # Update the status
    client.post(f'/update_status/{bug_id}', data={'status': 'In Progress'})

    # Verify the status and completion date
    updated_bug = db_session.get(Bug, bug_id)
    assert updated_bug.status == 'In Progress'
    assert updated_bug.completion_date is None
