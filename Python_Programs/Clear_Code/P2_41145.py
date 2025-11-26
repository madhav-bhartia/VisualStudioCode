grade = input("Enter you grade, 1-5\n-> ")

match grade:
    case "1":
        print("Very Good!, keep it up :)")
    case "2":
        print("Good!, keep it up, u can do it! :)")
    case "3":
        print("Average!, it's all right :) u have room to improve!")
    case "4":
        print("Okay!, keep it up :)")
    case "5":
        print("Needs Improvement!, u need to improve! u can still do it! :)")
    case _:
        print("Grade not recognised! ¯\_(ツ)_/¯")
