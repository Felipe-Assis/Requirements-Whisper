label student_test_start:
    $ student_reset()
    $ student_introduced = True
    jump student_city

testsuite student_life:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"
        run Start("student_test_start")
        advance until screen "student_city_screen"

    testcase conflict_reorganization_and_conversation:
        assert eval campaign_clock["image"] == "images/bg/cidade_dia.png" and campaign_clock["time"] == "16h"
        click id "student_schedule_open"
        advance until screen "student_schedule_screen"
        assert eval campaign_clock["image"] == "images/bg/quarto_noite.png" and campaign_clock["time"] == "20h"
        click id "student_tuesday_study"
        click id "student_thursday_rest"
        click id "student_thursday_workshop"
        assert screen "student_schedule_screen"
        assert eval student_schedule == {"tuesday": "study", "thursday": "rest"}
        assert eval "nada foi substituído" in student_feedback
        click id "student_clear_thursday"
        click id "student_thursday_workshop"
        click id "student_talk"
        advance until screen "student_schedule_screen"
        assert eval "horário regular" in student_agreement
        assert eval "terça" in student_agreement.lower()
        assert eval not student_agreement_pending()

    testcase course_and_save_keep_tip_agenda_visits_and_evidence:
        click id "student_map_workshop"
        pause until screen "student_location_screen"
        assert eval campaign_clock["image"] == "images/bg/oficina_dia.png" and campaign_clock["time"] == "16h"
        click id "student_object"
        assert eval "workshop" in student_evidence
        click id "student_course"
        pause until screen "student_location_screen"
        assert eval not student_course_done
        assert screen "student_location_screen"
        click id "student_location_schedule"
        advance until screen "student_schedule_screen"
        click id "student_thursday_workshop"
        click id "student_schedule_back"
        pause until screen "student_city_screen"
        click id "student_hotspot_workshop"
        pause until screen "student_location_screen"
        click id "student_course"
        pause until screen "student_course_confirmation"
        assert eval not student_course_done
        click id "student_course_cancel"
        advance until screen "student_schedule_screen"
        assert eval not student_course_done and student_schedule["thursday"] == "workshop"
        click id "student_schedule_back"
        pause until screen "student_city_screen"
        click id "student_map_workshop"
        pause until screen "student_location_screen"
        click id "student_course"
        pause until screen "student_course_confirmation"
        click id "student_course_confirm"
        advance until screen "student_location_screen"
        assert eval student_course_done
        assert eval campaign_clock["image"] == "images/bg/oficina.png" and campaign_clock["time"] == "20h"
        $ renpy.take_screenshot()
        $ renpy.save("qa-student-life")
        $ student_reset()
        $ renpy.load("qa-student-life")
        pause until screen "student_location_screen"
        assert eval student_course_done
        assert eval student_schedule["thursday"] == "workshop"
        assert eval student_visits == ["workshop"] and student_evidence == ["workshop"]
        click id "student_location_schedule"
        advance until screen "student_schedule_screen"
        click id "student_clear_thursday"
        click id "student_thursday_overtime"
        assert eval student_schedule["thursday"] == "workshop" and student_course_done
        assert eval "concluída" in student_feedback
        click id "student_tuesday_rest"
        assert eval student_schedule["tuesday"] == "rest"
        click id "student_clear_tuesday"
        click id "student_tuesday_study"
        assert eval student_schedule["tuesday"] == "study"
        click id "student_schedule_back"
        pause until screen "student_city_screen"
        click id "student_tip_open"
        pause until screen "student_tip_screen"
        click id "student_tip_close"
        pause until not screen "student_tip_screen"
        assert screen "student_city_screen"

    testcase course_is_optional_and_return_keeps_projects_available:
        click id "student_city_back"
        pause until screen "campaign_hub_screen"
        assert eval not student_course_done
        click id "campaign_project_expenses"
        advance until screen "exp_investigation"

    testcase study_reservation_selects_night_without_blocking_day_visit:
        click id "student_map_campus"
        pause until screen "student_location_screen"
        assert eval campaign_clock["image"] == "images/bg/campus.png" and campaign_clock["time"] == "16h"
        click id "student_location_schedule"
        advance until screen "student_schedule_screen"
        click id "student_tuesday_study"
        click id "student_schedule_back"
        pause until screen "student_city_screen"
        click id "student_map_campus"
        pause until screen "student_location_screen"
        assert eval campaign_clock["image"] == "images/bg/campus_noite.png" and campaign_clock["time"] == "20h"
        assert eval campaign_clock["day"] == "Terça-feira" and not student_course_done
