def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars


    global total_runn
    global tired
    global total_stars
    global cur_star
    global resting_time
    global star_activity
    global star_time

    global test_hedons
    global total_star_time

    cur_hedons = 0
    cur_health = 0

    cur_star = False
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000

    total_runn = 180
    total_stars = 0
    tired = False
    resting_time = 0
    star_activity = None
    star_time = 0

    test_hedon = 0

    total_star_time = 0


def star_can_be_taken(activity):
    global last_activity, cur_time, cur_star
    global last_activity_duration

    if star_activity == activity and star_time == 0 and bored_with_stars == False:
        cur_star = True
        return cur_star

    else:
        cur_star = False
        return cur_star


def perform_activity(activity, duration):
    ''''Start an activity over a time interval
    activity = activity chosen, can be running, textbooks or resting, a string
    duration = time spent doing activity in minutes, positive integer'''

    global cur_health, cur_time, cur_hedons, cur_star, bored_with_stars
    global total_runn
    global last_activity, resting_time, tired, star_time



    if activity == "running":
        resting_time = 0

        #health points
        if (total_runn - duration) > 0:
            cur_health += duration*3
            total_runn -= duration
            cur_time += duration

        elif (total_runn - duration) < 0:
            if total_runn > 0:
                cur_health += ((total_runn*3)+(duration-total_runn)*1)
                total_runn -= duration
                cur_time += duration

            elif total_runn < 0:
                cur_health += duration*1
                cur_time += duration

        #hedons
        if star_can_be_taken(activity) == False:
            if 0 <= resting_time < 120 and (last_activity == "textbooks" or last_activity == "running"):
                tired = True

            if tired == True:

                cur_hedons -= 2*duration

            elif tired == False:
                if 0 < duration <= 10:
                    cur_hedons += 2*duration

                elif duration > 10:
                    cur_hedons += 10*2
                    cur_hedons -= 2*(duration-10)


        if star_can_be_taken(activity) == True:
            if tired == True:
                if 0 < duration <= 10:
                    cur_hedons += (3-2)*duration

                elif duration > 10:
                    cur_hedons += 10
                    cur_hedons += (duration - 10)*-2

            if tired == False:
                if 0 < duration <= 10:
                    cur_hedons += duration*(3+2)

                elif duration > 10:
                    cur_hedons += 10*(3+2)
                    cur_hedons += (duration-10)*-2



            cur_star = False




        last_activity = "running"
        star_time += 1



    if activity == "resting":

        total_runn = 180
        cur_time += duration
        resting_time += duration

        if resting_time >= 120 or (cur_time - duration) == 0:
            tired = False

        elif resting_time < 120 and last_activity != "resting":
            tired = True

        last_activity = "resting"
        star_time += 1



    if activity == "textbooks":
        total_runn = 180
        cur_health += duration *2
        cur_time += duration
        resting_time = 0

        #Hedons
        if star_can_be_taken(activity) == False:
            if 0 <= resting_time < 120 and (last_activity == "textbooks" or last_activity == "running"):
                tired = True


            if tired == True:
                cur_hedons -= 2*duration

            elif tired == False:
                if 0 < duration <= 20:
                    cur_hedons += 1*duration

                elif duration > 20:
                    cur_hedons += 20
                    cur_hedons -= 1*(duration-20)

        if star_can_be_taken(activity) == True:

            if tired == True:
                if 0 < duration <= 10:
                    cur_hedons += (3-2)*duration
                elif duration > 10:
                    cur_hedons += 10*(3-2)
                    cur_hedons += (duration-10)*(-2)

            if tired == False:
                if 0 < duration <= 10:
                    cur_hedons += duration*(3+1)

                elif 10 < duration < 20:
                    cur_hedons += 10*(3+1)
                    cur_hedons += (duration-10)

                elif duration > 20:
                    cur_hedons += 10*(3+1)
                    cur_hedons += 10
                    cur_hedons += -1*(duration-20)

            cur_star = False


        last_activity = "textbooks"
        star_time += 1

    else:
        pass



def get_cur_hedons():
    '''Return amount of hedon (fun points) collected by the user
    '''

    global cur_hedons
    return cur_hedons


def get_cur_health():
    '''Return amount of health points collected by the user
    '''

    global cur_health
    return cur_health


def offer_star(activity):
    global star_activity, cur_time, bored_with_stars, total_stars
    global last_activity_duration, star_time, total_star_time

    total_stars += 1


    if total_stars == 1:
        star_activity = activity
        star_time = 0
        total_star_time = cur_time

    elif total_stars == 2 and (cur_time - total_star_time) < 120:
        star_activity = activity
        star_time = 0
        total_star_time = cur_time - total_star_time

    elif total_stars == 3 and (cur_time - total_star_time) > 120:
        total_star_time = 0
        star_activity = activity
        star_time = 0


    else:
        bored_with_stars = True



def most_fun_activity_minute():
    '''Give activity that would give the most hedons for 1 minute to user'''


    global cur_star, last_activity, star_activity
    global cur_hedons


    if star_time == 0 and total_stars >= 1 and bored_with_stars == False:
        return star_activity

    elif tired == True:
        return "resting"

    elif last_activity == "running" or last_activity == "textbooks": #they would become tired if they did these again
        return "resting"

    elif tired == False:
        return "running"



################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            #-20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())            #90 = 30 * 3
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  #running
    perform_activity("textbooks", 30)
    print(get_cur_health())            #150 = 90 + 30*2
    print(get_cur_hedons())            #-80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            #210 = 150 + 20 * 3
    print(get_cur_hedons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            #700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            #-430 = -90 + 170 * (-2)