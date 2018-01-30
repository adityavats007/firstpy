##// CURRENT:
##// list of topics by {TOPIC:[["TITLE", "URL"]]}
##
##// FUTURE:
##////list of topics by {TOPIC:[["TITLE", "URL", "TAGS"],
##////                          ["TITLE", "URL", "TAGS"]]}

def Content():
##    //             Suggest Branches for next steps
##    //             If liked: Matplotlib, link to data analysis or Pandas maybe
##    //             If liked: GUI stuff: Kivy, PyGame, Tkinter
##    //             if liked: Text and word-based: NLTK


    # MAIN : [TITLE, URL, BODY_TEXT (LIST), HINTS(LIST)]
    TOPIC_DICT = {"Elementary Education":[["Sarva Shiksha Abhiyan","/Elementary_Education_one/"],
                            ["Mid Day Meal","/Elementary_Education_two/"],
                            ["Strengthening of Teachers Training Institute","/Elementary_Education_three/"],
                            ["Schemes for Infrastucture Development of Private Aided/Unaided Minority Institutes (IDMI)","/Elementary_Education_four/"],
                            ["Mahila Samakhya","/Elementary_Education_five/"],
                            ["Strengthening for providing quality Education in Madrassas ( SPQEM)","/Elementary_Education_six/"]],
                
                  
                  "Secondary Education":[["Rashtriya Madhyamik Shiksha Abhiyan (RMSA)","/Secondary_Education_one/"],
                           ["Inclusive Education for Disable at Secondary Stage ( IEDSS )","/Secondary_Education_two/"],
                           ["Incentives to Girls at Secondary Stage","/Secondary_Education_three/"],
                           ["National Merit cum Means Scholarship","/Secondary_Education_four/"],
                           ["Financial Assistance for Appointment of language Teachers","/Secondary_Education_five/"],
                           ["Adolescence Education Programme","/Secondary_Education_six/"],
                           ["Girls Hostel","/Secondary_Education_seven/"],
                           ["Model School","/Secondary_Education_eight/"],
                           ["ICT at School","/Secondary_Education_nine/"],
                           ["Vocationalisation of Secondary Education","/Secondary_Education_ten/"],
                           ["Model School Under Public- Private Partnership(PPP)Mode","/Secondary_Education_eleven/"],],

                  
                  "Higher Education":[["Rashtriya Ucchatar Shiksha Abhiyan (RUSA)","/Higher_Education_one/"],
                                      ["National Initiative for Design Innovation","/Higher_Education_two/"],
                                      ["National Research Professorship (NRP)","/Higher_Education_three/"],
                                      ["Establishment of New Central Universities","/Higher_Education_four/"],
                                      ["Indira Gandhi National Tribal University","/Higher_Education_five/"],
                                      ["Establishment of 14 World Class Central Universities","/Higher_Education_six/"],
                                      ["Setting up of 374 Degree Colleges in Educationally Backward Districts","/Higher_Education_seven/"],
                                      ["Scheme for incentivising state governments for expansion of higher education institutions","/Higher_Education_eight/"],
                                      ["Central Sector Interest Subsidy Scheme, 2009 on Model Education Loan Scheme of IBA","/Higher_Education_nine/"],
                                      ["Construction of girls hostels","/Higher_Education_ten/"],
                                      ["Supporting uncovered state universities and colleges","/Higher_Education_eleven/"],
                                      ["Additional assistance to about 160 already covered universities and about 5500 colleges","/Higher_Education_twelve/"],
                                      ["Strengthening science based higher education and research in universities","/Higher_Education_thirteen/"],
                                      ["Inter universities research institute for policy and evaluation","/Higher_Education_fourteen/"],
                                      ["Schemes Implemented through Autonomous Organisations","/Higher_Education_fifteen/"]],


                  
                  "Technical Education":[["Sub-Mission on Polytechnics under the Coordinated Action for Skill Development","/polytechnics/"],
                                         ["Scheme of Apprenticeship Training","/apprenticeship/"],
                                         ["Support For Distance Education & Web Based Learning (NPTEL)","/nptel_support/"],
                                         ["Indian National Digital Library in Engineering, Science & Technology (INDEST-AICTE) Consortium","/Indest/"],
                                         ["National Programme of Earthquake Engineering Education (NPEEE)","/Npeee/"],
                           ["Technology Development Mission","/tech_dev_mission/"],
                           ["Direct Admission of Students Abroad","/direct_abroad_admission/"],
                           ["Scheme for Upgrading existing Polytechnics to Integrate the Physically Disabled in the mainstream of Technical and Vocational Education","/scheme_for_upgrade/"],
                           ["Setting up 20 new IIITs","/setting_up_IIT/"],],

                  
                  "Adult Education":[["Saakshar Bharat","/saakshar_bharat/"],
                            ["State Resource Center (SRCs)","/srcs/"],
                            ["Jan Shikshan Sansthans(JSSs)","/jss/"],
                            ["Assistance to Voluntary Agencies","/Voluntary_agencies/"],],

                  
                  "Teacher Education":[["Centrally Sponsored Scheme","/centrally_sponsored_scheme/"],],
                  
                            }


    return TOPIC_DICT








if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])
	  
