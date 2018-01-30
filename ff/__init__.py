
from content_management import Content

from dbconnect import connection

from flask import Flask, render_template, flash, request, url_for, redirect, session


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import TextField , validators, PasswordField, BooleanField
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps
import gc


TOPIC_DICT=Content()



app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/',methods=['GET','POST'])
def homepage():
       error=''
       try:
        c, conn=connection()
        if request.method=="POST":
        
          sql_check_reg= "SELECT * FROM users WHERE username = %s"
          data = c.execute(sql_check_reg, (request.form['username'],))
                             
          data=c.fetchone()[2]
          if  sha256_crypt.verify(request.form['password'],data):
              session['logged_in']=True
              session['username']=request.form['username']
#
              flash("logged in")
              return redirect(url_for('dashboard'))
          else:
              error="Invalid credentials"
      
        gc.collect()
        return render_template("main.html",error=error)
       except Exception as e:
        error="Invalid credentials"
        flash("invalid credentials")
        return render_template("main.html",error=error)
      # try:
       #     if request.method == "POST" and form.validate():
         #       username  = form.username.data
        #        email = form.email.data
         #       password = sha256_crypt.encrypt((str(form.password.data)))
         #       c, conn = connection()
           
       

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html" , TOPIC_DICT = TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login_page'))

    return wrap

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('dashboard'))
		

@app.route('/login/',methods=['GET','POST'])
def login_page():
    error=''
    try:
        c, conn=connection()
        if request.method=="POST":
        
          sql_check_reg= "SELECT * FROM users WHERE username = %s"
          data = c.execute(sql_check_reg, (request.form['username'],))
                             
          data=c.fetchone()[2]
          if  sha256_crypt.verify(request.form['password'],data):
              session['logged_in']=True
              session['username']=request.form['username']

              flash("logged in")
              return redirect(url_for('dashboard'))
          else:
              error="Invalid credentials"
      
        gc.collect()
        return render_template("login.html",error=error)
    except Exception as e:
        error="Invalid credentials"
        flash("invalid credentials")
        return render_template("login.html",error=error)


class RegistrationForm(FlaskForm):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
    

		

@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form=RegistrationForm(csrf_enabled=False)
        if request.method == "POST" and form.validate():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            sql_check_reg= "SELECT * FROM users WHERE username = %s"
            x = c.execute(sql_check_reg, (username,))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                sql_insert_reg = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
                c.execute(sql_insert_reg, (username, password, email))
                #c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                 #         (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))
                
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))
#
@app.route(TOPIC_DICT["Higher Education"][0][1])
def Rashtriya_Ucchatar_Shiksha_Abhiyan_RUSA():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("Higher_Education_one.html")




@app.route(TOPIC_DICT["Higher Education"][1][1], methods=['GET', 'POST'])
def National_Initiative_for_Design_Innovation():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("Higher_Education_two.html")




@app.route(TOPIC_DICT["Higher Education"][2][1], methods=['GET', 'POST'])
def National_Research_Professorship_NRP():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("Higher_Education_three.html")




@app.route(TOPIC_DICT["Higher Education"][3][1], methods=['GET', 'POST'])
def Establishment_of_New_Central_Universities():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_four.html")




@app.route(TOPIC_DICT["Higher Education"][4][1], methods=['GET', 'POST'])
def Indira_Gandhi_National_Tribal_University():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_five.html")




@app.route(TOPIC_DICT["Higher Education"][5][1], methods=['GET', 'POST'])
def Establishment_of_14_World_Class_Central_Universities():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_six.html")




@app.route(TOPIC_DICT["Higher Education"][6][1], methods=['GET', 'POST'])
def Setting_up_of_374_Degree_Colleges_in_Educationally_Backward_Districts():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_seven.html")




@app.route(TOPIC_DICT["Higher Education"][7][1], methods=['GET', 'POST'])
def Scheme_for_incentivising_state_governments_for_expansion_of_higher_education_institutions():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_eight.html")




@app.route(TOPIC_DICT["Higher Education"][8][1], methods=['GET', 'POST'])
def Central_Sector_Interest_Subsidy_Scheme_2009_on_Model_Education_Loan_Scheme_of_IBA():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_nine.html")




@app.route(TOPIC_DICT["Higher Education"][9][1], methods=['GET', 'POST'])
def Construction_of_girls_hostels():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_ten.html")




@app.route(TOPIC_DICT["Higher Education"][10][1], methods=['GET', 'POST'])
def Supporting_uncovered_state_universities_and_colleges():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_eleven.html")




@app.route(TOPIC_DICT["Higher Education"][11][1], methods=['GET', 'POST'])
def Additional_assistance_to_about_160_already_covered_universities_and_about_5500_colleges():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_twelve.html")




@app.route(TOPIC_DICT["Higher Education"][12][1], methods=['GET', 'POST'])
def Strengthening_science_based_higher_education_and_research_in_universities():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_thirteen.html")




@app.route(TOPIC_DICT["Higher Education"][13][1], methods=['GET', 'POST'])
def Inter_universities_research_institute_for_policy_and_evaluation():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_fourteen.html")




@app.route(TOPIC_DICT["Higher Education"][14][1], methods=['GET', 'POST'])
def Schemes_Implemented_through_Autonomous_Organisations():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Higher Education/Higher_Education_fifteen.html")




@app.route(TOPIC_DICT["Adult Education"][0][1], methods=['GET', 'POST'])
def Saakshar_Bharat():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("saakshar_bharat.html")




@app.route(TOPIC_DICT["Adult Education"][1][1], methods=['GET', 'POST'])
def State_Resource_Center_SRCs():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Adult Education/srcs.html")




@app.route(TOPIC_DICT["Adult Education"][2][1], methods=['GET', 'POST'])
def Jan_Shikshan_SansthansJSSs():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Adult Education/jss.html")




@app.route(TOPIC_DICT["Adult Education"][3][1], methods=['GET', 'POST'])
def Assistance_to_Voluntary_Agencies():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Adult Education/Voluntary_agencies.html")




@app.route(TOPIC_DICT["Secondary Education"][0][1], methods=['GET', 'POST'])
def Rashtriya_Madhyamik_Shiksha_Abhiyan_RMSA():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_one.html")




@app.route(TOPIC_DICT["Secondary Education"][1][1], methods=['GET', 'POST'])
def Inclusive_Education_for_Disable_at_Secondary_Stage__IEDSS_():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_two.html")




@app.route(TOPIC_DICT["Secondary Education"][2][1], methods=['GET', 'POST'])
def Incentives_to_Girls_at_Secondary_Stage():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_three.html")




@app.route(TOPIC_DICT["Secondary Education"][3][1], methods=['GET', 'POST'])
def National_Merit_cum_Means_Scholarship():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_four.html")




@app.route(TOPIC_DICT["Secondary Education"][4][1], methods=['GET', 'POST'])
def Financial_Assistance_for_Appointment_of_language_Teachers():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_five.html")




@app.route(TOPIC_DICT["Secondary Education"][5][1], methods=['GET', 'POST'])
def Adolescence_Education_Programme():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_six.html")




@app.route(TOPIC_DICT["Secondary Education"][6][1], methods=['GET', 'POST'])
def Girls_Hostel():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_seven.html")




@app.route(TOPIC_DICT["Secondary Education"][7][1], methods=['GET', 'POST'])
def Model_School():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_eight.html")




@app.route(TOPIC_DICT["Secondary Education"][8][1], methods=['GET', 'POST'])
def ICT_at_School():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_nine.html")




@app.route(TOPIC_DICT["Secondary Education"][9][1], methods=['GET', 'POST'])
def Vocationalisation_of_Secondary_Education():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_ten.html")




@app.route(TOPIC_DICT["Secondary Education"][10][1], methods=['GET', 'POST'])
def Model_School_Under_Public__Private_PartnershipPPPMode():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Secondary Education/Secondary_Education_eleven.html")




@app.route(TOPIC_DICT["Teacher Education"][0][1], methods=['GET', 'POST'])
def Centrally_Sponsored_Scheme():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Teacher Education/centrally_sponsored_scheme.html")




@app.route(TOPIC_DICT["Technical Education"][0][1], methods=['GET', 'POST'])
def Sub_Mission_on_Polytechnics_under_the_Coordinated_Action_for_Skill_Development():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/polytechnics.html")




@app.route(TOPIC_DICT["Technical Education"][1][1], methods=['GET', 'POST'])
def Scheme_of_Apprenticeship_Training():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/apprenticeship.html")




@app.route(TOPIC_DICT["Technical Education"][2][1], methods=['GET', 'POST'])
def Support_For_Distance_Education_and_Web_Based_Learning_NPTEL():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/nptel_support.html")




@app.route(TOPIC_DICT["Technical Education"][3][1], methods=['GET', 'POST'])
def Indian_National_Digital_Library_in_Engineering_Science_and_Technology_INDEST_AICTE_Consortium():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/Indest.html")




@app.route(TOPIC_DICT["Technical Education"][4][1], methods=['GET', 'POST'])
def National_Programme_of_Earthquake_Engineering_Education_NPEEE():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/Npeee.html")




@app.route(TOPIC_DICT["Technical Education"][5][1], methods=['GET', 'POST'])
def Technology_Development_Mission():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/tech_dev_mission.html")




@app.route(TOPIC_DICT["Technical Education"][6][1], methods=['GET', 'POST'])
def Direct_Admission_of_Students_Abroad():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/direct_abroad_admission.html")




@app.route(TOPIC_DICT["Technical Education"][7][1], methods=['GET', 'POST'])
def Scheme_for_Upgrading_existing_Polytechnics_to_Integrate_the_Physically_Disabled_in_the_mainstream_of_Technical_and_Vocational_Education():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/scheme_for_upgrade.html")




@app.route(TOPIC_DICT["Technical Education"][8][1], methods=['GET', 'POST'])
def Setting_up_20_new_IIITs():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Technical Education/setting_up_IIT.html")




@app.route(TOPIC_DICT["Elementary Education"][0][1], methods=['GET', 'POST'])
def Sarva_Shiksha_Abhiyan():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_one.html")




@app.route(TOPIC_DICT["Elementary Education"][1][1], methods=['GET', 'POST'])
def Mid_Day_Meal():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_two.html")




@app.route(TOPIC_DICT["Elementary Education"][2][1], methods=['GET', 'POST'])
def Strengthening_of_Teachers_Training_Institute():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_three.html")




@app.route(TOPIC_DICT["Elementary Education"][3][1], methods=['GET', 'POST'])
def Schemes_for_Infrastucture_Development_of_Private_AidedUnaided_Minority_Institutes_IDMI():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_four.html")




@app.route(TOPIC_DICT["Elementary Education"][4][1], methods=['GET', 'POST'])
def Mahila_Samakhya():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_five.html")




@app.route(TOPIC_DICT["Elementary Education"][5][1], methods=['GET', 'POST'])
def Strengthening_for_providing_quality_Education_in_Madrassas__SPQEM():
    #update_user_tracking()
    #completed_percentages = topic_completion_percent()
    return render_template("/Elementary Education/Elementary_Education_six.html")


if __name__ == "__main__":
    
    app.run()
   
