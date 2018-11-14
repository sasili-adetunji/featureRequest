from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import FeatureForm
from .. import db
from ..models import Feature, Client


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user:
        abort(403)


# feature requests Views


@admin.route('/features', methods=['GET', 'POST'])
@login_required
def list_features():
    """
    List all feature requests
    """
    check_admin()

    features = Feature.query.all()

    return render_template('features/features.html',
                           features=features, title="Features")


@admin.route('/features/add', methods=['GET', 'POST'])
@login_required
def add_feature():
    """
    Add a feature request to the database
    """
    check_admin()

    add_feature = True

    form = FeatureForm()
    if form.validate_on_submit():

        clients = Client.query.filter_by(client=form.client.data).order_by("client_priority desc")
        priority_point = 1
        if priority_point < clients.count():
            for client_row in clients:
                new_client  = client_row.client;
                new_client_priority = client_row.client_priority;

                if new_client_priority >= form.client_priority.data:
                    new_c = Client(client=new_client,
                                client_priority=new_client_priority + 1,
                        )
                    db.session.add(new_c)
                    db.session.commit()
        feature = Feature(title=form.title.data,
                          description=form.description.data,
                          product_area=form.product_area.data,
                          target_date=form.target_date.data,
                          client=new_c,

                  )
        try:
            # add feature to the database
            db.session.add(feature)
            db.session.commit()
            flash('You have successfully added a new feature requests.')
        except:
            # in case feature name already exists
            flash('Error: feature requests name already exists.')

        # redirect to features page
        return redirect(url_for('admin.list_features'))

    # load feature template
    return render_template('features/feature.html', action="Add",
                           add_feature=add_feature, form=form,
                           title="Add Feature")


@admin.route('/features/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_feature(id):
    """
    Edit a feature request
    """
    check_admin()

    add_feature = False

    feature = Feature.query.get_or_404(id)
    form = FeatureForm(obj=feature)
    if form.validate_on_submit():
        feature.title = form.title.data
        feature.description = form.description.data
        feature.client.client = form.client.data
        feature.client.client_priority = form.client_priority.data
        feature.target_date = form.target_date.data
        feature.product_area = form.product_area.data
        db.session.commit()
        flash('You have successfully edited the feature requests.')

        # redirect to the feature page
        return redirect(url_for('admin.list_features'))

    form.description.data = feature.description
    form.title.data = feature.title
    form.client.data = feature.client.client
    form.client_priority.data = feature.client.client_priority
    form.target_date.data = feature.target_date
    form.product_area.data = feature.product_area

    return render_template('features/feature.html', action="Edit",
                           add_feature=add_feature, form=form,
                           feature=feature, title="Edit Feature")


@admin.route('/features/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_feature(id):
    """
    Delete a feature request from the database
    """
    check_admin()

    feature = Feature.query.get_or_404(id)
    client = Client.query.get_or_404(feature.client.id)
    db.session.delete(feature)
    db.session.commit()
    db.session.delete(client)
    db.session.commit()

    flash('You have successfully deleted the feature requests.')

    # redirect to the feature page
    return redirect(url_for('admin.list_features'))

