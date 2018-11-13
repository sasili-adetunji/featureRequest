from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import FeatureForm
from .. import db
from ..models import Feature


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user:
        abort(403)


# Department Views


@admin.route('/features', methods=['GET', 'POST'])
@login_required
def list_features():
    """
    List all departments
    """
    check_admin()

    features = Feature.query.all()

    return render_template('features/features.html',
                           features=features, title="Features")


@admin.route('/features/add', methods=['GET', 'POST'])
@login_required
def add_feature():
    """
    Add a department to the database
    """
    check_admin()

    add_feature = True

    form = FeatureForm()
    if form.validate_on_submit():
        feature = Feature(title=form.title.data,
                          description=form.description.data,
                          product_area=form.product_area.data,
                          target_date=form.target_date.data,
                          client=form.client.data,

                  )
        try:
            # add feature to the database
            db.session.add(feature)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case feature name already exists
            flash('Error: department name already exists.')

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
    Edit a feature
    """
    check_admin()

    add_feature = False

    feature = Feature.query.get_or_404(id)
    form = FeatureForm(obj=feature)
    if form.validate_on_submit():
        feature.title = form.title.data
        feature.description = form.description.data
        feature.client = form.client.data
        feature.client_priority = form.client_priority.data
        feature.target_date = form.target_date.data
        feature.product_area = form.product_area.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the feature page
        return redirect(url_for('admin.list_features'))

    form.description.data = feature.description
    form.title.data = feature.title
    form.client.data = feature.client
    form.client_priority.data = feature.client_priority
    form.target_date.data = feature.target_date
    form.product_area.data = feature.product_area

    return render_template('features/feature.html', action="Edit",
                           add_feature=add_feature, form=form,
                           feature=feature, title="Edit Feature")


@admin.route('/features/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_feature(id):
    """
    Delete a department from the database
    """
    check_admin()

    feature = Feature.query.get_or_404(id)
    db.session.delete(feature)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the feature page
    return redirect(url_for('admin.list_features'))

