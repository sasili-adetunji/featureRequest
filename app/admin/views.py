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
        new_c = None
        # import pdb; pdb.set_trace()
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
        else:
            new_c = Client(client=form.client.data,
                            client_priority=form.client_priority.data,
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
