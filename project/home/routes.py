from datetime import datetime

from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import login_required, current_user

from project import db
from project.models import FeatureRequest
from project.home.forms import FeatureRequestForm


# config
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


def reorder_client_priority(client_input, client_priority_input):
    request_client = FeatureRequest.query.filter_by(
        client=client_input, author=current_user).order_by('client_priority').all()
    for item in request_client:
        if client_priority_input <= item.client_priority:
            item.client_priority += 1
            db.session.commit()


# routes

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    requests_all = FeatureRequest.query.filter_by(
        author=current_user).order_by('client_priority').all()
    form = FeatureRequestForm()
    if form.validate_on_submit():
        reorder_client_priority(form.client.data, form.client_priority.data)
        request_new = FeatureRequest(title=form.title.data, description=form.description.data, client=form.client.data,
                                     client_priority=form.client_priority.data, target_date=form.target_date.data, product_area=form.product_area.data, author=current_user.id)
        db.session.add(request_new)
        db.session.commit()
        flash('Your Feature Request has been Added!', 'success')
        return redirect(url_for('home.home'))
    return render_template('home.html', form=form, requests=requests_all, now=datetime.utcnow())


@home_blueprint.route("/request/<int:featurerequest_id>", methods=['GET', 'POST'])
@login_required
def detail(featurerequest_id):
    form = FeatureRequestForm()
    request_detail = FeatureRequest.query.get_or_404(featurerequest_id)
    if request.method == 'GET' and request_detail.author == current_user:
        form.title.data = request_detail.title
        form.description.data = request_detail.description
        form.client.data = request_detail.client
        form.client_priority.data = request_detail.client_priority
        form.target_date.data = request_detail.target_date
        form.product_area.data = request_detail.product_area
    elif request.method == 'POST' and request_detail.author == current_user and form.validate_on_submit():
        reorder_client_priority(form.client.data, form.client_priority.data)
        request_detail.title = form.title.data
        request_detail.description = form.description.data
        request_detail.client = form.client.data
        request_detail.client_priority = form.client_priority.data
        request_detail.target_date = form.target_date.data
        request_detail.product_area = form.product_area.data
        db.session.commit()
        flash('Your Feature Request has been updated!', 'success')
        return redirect(url_for('home.home'))
    else:
        abort(403)
    return render_template('detail.html', form=form, request=request_detail, now=datetime.utcnow())


@home_blueprint.route("/request/<int:featurerequest_id>/delete", methods=['POST'])
@login_required
def delete(featurerequest_id):
    request_detail = FeatureRequest.query.get_or_404(featurerequest_id)
    if request_detail.author != current_user:
        abort(403)
    request_client = FeatureRequest.query.filter_by(
        client=request_detail.client, author=current_user).all()
    for item in request_client:
        if item.client_priority != 1:
            item.client_priority -= 1
            db.session.commit()
    db.session.delete(request_detail)
    db.session.commit()
    flash('Your post has been deleted!', 'danger')
    return redirect(url_for('home.home'))
