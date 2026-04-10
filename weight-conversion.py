print("\n Welcome to Weight & BMI Calculator!")

#User Info
username = input("Please enter your name: ").strip()

age = input("Enter your age: ").strip()

if age == "":
    print("Error: Please enter your age!")

else:
    try:
        user_age = int(age)

        # INPUTS
        weight_unit = input("Is your weight kg or lb?: ").strip().lower()
        weight_input = input("Please enter your weight: ").strip()

        height_unit = input("Is your height meters or inches?: ").strip().lower()
        height_input = input("Please enter your height: ").strip()

        if weight_input == "" or height_input == "":
            print("Error: Weight and height cannot be empty!")

        else:
            try:
                weight = float(weight_input)
                height = float(height_input)

                # Convert Weight
                if weight_unit == "lb":
                    weight = weight * 0.453592
                elif weight_unit != "kg":
                    print("Invalid weight unit!")
                    weight = 0

                # Convert Height
                if height_unit == "in" or height_unit == "inches":
                    height = height * 0.0254
                elif height_unit != "meters":
                    print("Invalid height unit!")
                    height = 0

                # Validation
                if weight <= 0 or height <= 0:
                    print("Error: Invalid weight or height entered!")

                else:
                    bmi = weight / (height * height)

                    print(f"\nHello {username}!")
                    print(f"Your BMI is: {round(bmi, 2)}")

                  #Questions
                    def ask_yes_no(question):
                        answer = input(question + " (Yes/No): ").strip().lower()
                        if answer == "yes" or answer == "no":
                            return answer
                        else:
                            print("Invalid input! Please answer Yes or No only.")
                            return ask_yes_no(question)

                    #Underweight
                    if bmi < 18.5:
                        print("\nStatus: Underweight")
                        print("Recommendation: Increase calorie intake, eat protein-rich food, and maintain regular meals.")

                        ask_yes_no("PAR-Q: Do you eat at least 3 meals a day?")
                        ask_yes_no("PAR-Q: Do you often feel low energy?")
                        ask_yes_no("PAR-Q: Have you consulted a doctor before about your weight?")

                        print("\n Please be advised:")
                        print("Being underweight may affect your health and immune system.")
                        print("It is recommended to consult a doctor or nutritionist for proper guidance.")

                   #Healthy
                    elif bmi < 25:
                        print("\nStatus: Healthy")
                        print("Recommendation: Maintain your lifestyle, stay active, and eat balanced meals.")

                        ask_yes_no("PAR-Q: Do you exercise at least 3 times a week?")
                        ask_yes_no("PAR-Q: Do you drink enough water daily?")
                        ask_yes_no("PAR-Q: Do you feel physically active most days?")

                        print("\n Please be advised:")
                        print("Being healthy may be of healthy but please stay active.")
                        print("Consider adopting a healthier lifestyle and consulting a health professional.")
                  
                    #Overweight
                    elif bmi < 30:
                        print("\nStatus: Overweight")
                        print("Recommendation: Start light exercise, reduce sugar intake, and control portions.")

                        ask_yes_no("PAR-Q: Do you currently exercise?")
                        ask_yes_no("PAR-Q: Are you willing to start daily walking?")
                        ask_yes_no("PAR-Q: Do you often consume fast food or sugary drinks?")

                        print("\n Please be advised:")
                        print("Being overweight may increase risk of health problems.")
                        print("Consider adopting a healthier lifestyle and consulting a health professional.")

                    #Obese
                    else:
                        print("\nStatus: Obese")
                        print("Recommendation: Daily walking, structured diet plan, and medical consultation.")

                        ask_yes_no("PAR-Q: Have you ever visited a doctor for weight concerns?")
                        ask_yes_no("PAR-Q: Do you experience fatigue during normal activities?")
                        ask_yes_no("PAR-Q: Are you willing to start a health improvement plan?")

                        print("\n  Please be advised:")
                        print("Obesity increases the risk of serious health conditions.")
                        print("It is strongly recommended to consult a doctor or nutritionist.")

            except ValueError:
                print("Error: Please enter numbers only!")

    except ValueError:
        print("Error: Age must be a number!")