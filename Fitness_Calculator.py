import requests
import json


class IBS:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


class BMI(IBS):
    def __init__(self, height, weight):
        super().__init__(height, weight)


class IdealWeight(IBS):
    def __init__(self, gender, height, weight):
        self.gender = gender
        super().__init__(height, weight)


class FBS(IdealWeight):
    def __init__(self, height, weight, gender, neck, hip, waist, goalweight):
        self.neck = neck
        self.hip = hip
        self.waist = waist
        self.goalweight = goalweight
        super().__init__(gender, height, weight)


n = 1


def inputnum(st):
    print('Please enter your ' + str(st) + ':')
    while n:
        try:
            a = int(input())
        except ValueError:
            print('ERROR!!!\n Please enter a number: ')
        if a >= 0:
            break
    return a


def getgen():
    while n:
        try:
            x = int(input('\n'
                          'select gender\n'
                          '1 = Male\n'
                          '2 = Female\n'))

        except ValueError:
            print("ERROR!!!\nInput 1 or 2 only")
        if 1 <= x <= 2:
            break
        else:
            print("ERROR!!!\nInput 1 or 2 only")
    if x == 1:
        g = 'male'
    else:
        g = 'female'
    return g


while n == 1:
    while n:
        try:
            d = int(input('\n'
                          'Choose Your Request:\n'
                          '1- Ideal Weight\n'
                          '2- BMI\n'
                          '3- Full Body Stats\n'))
        except ValueError:
            print('ERROR!!!\nChoose between 1 to 3')
        if 1 <= d <= 3:
            break
        else:
            print('ERROR!!!\nChoose an option: ')

    if d == 1:
        p1 = IdealWeight(
            gender=getgen(),
            height=inputnum(st='height'),
            weight=inputnum(st='weight')
        )

        url = "https://fitness-api.p.rapidapi.com/fitness"

        payload = 'height=' + str(p1.height) + \
                  '&weight=' + str(p1.weight) + \
                  '&gender=' + str(p1.gender)
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "acb0accbadmshe4978232b5cce71p154a51jsna8f8c6a881e9",
            'x-rapidapi-host': "fitness-api.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers).json()
        value = response['idealBodyWeight']['hamwi']['metric']['value']
        print('Your ideal weight is: ' + str(value) + 'Kg')

    if d == 2:
        p1 = BMI(
            height=inputnum(st='height'),
            weight=inputnum(st='weight')
        )

        url = "https://fitness-api.p.rapidapi.com/fitness"

        payload = "height=" + str(p1.height) + \
                  "&weight=" + str(p1.weight)
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "acb0accbadmshe4978232b5cce71p154a51jsna8f8c6a881e9",
            'x-rapidapi-host': "fitness-api.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers).json()
        value = response['bodyMassIndex']['value']
        con = response['bodyMassIndex']['conclusion']
        print('Your BMI is: ', value, 'Kg/m2', '\nYour body status is:', con)

    if d == 3:
        p1 = FBS(
            gender=getgen(),
            height=inputnum(st='height'),
            weight=inputnum(st='weight'),
            neck=inputnum(st='neck circumference'),
            hip=inputnum(st='hip circumference'),
            waist=inputnum(st='waist circumference'),
            goalweight=inputnum(st='goal weight')

        )

        url = "https://fitness-api.p.rapidapi.com/fitness"

        payload = "height=" + str(p1.height) + \
                  "&weight=" + str(p1.weight) + \
                  "&gender=" + str(p1.gender) + \
                  "&neck=" + str(p1.neck) + \
                  "&hip=" + str(p1.hip) + \
                  "&waist=" + str(p1.waist) + \
                  "&goalWeight=" + str(p1.goalweight)
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "acb0accbadmshe4978232b5cce71p154a51jsna8f8c6a881e9",
            'x-rapidapi-host': "fitness-api.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers).json()

        bmi = response['bodyMassIndex']['value']
        bmicon = response['bodyMassIndex']['conclusion']
        bfp = response['bodyFatPercentage']['dod']['value']
        bfpcon = response['bodyFatPercentage']['dod']['conclusion']
        lbm = response['leanBodyMass']['dod']['value']
        rdeec = response['restingDailyEnergyExpenditure']['dod']['calories']['value']
        ibw = response['idealBodyWeight']['hamwi']['metric']['value']
        wthr = response['waistToHipRatio']['value']
        wthrcon = response['waistToHipRatio']['conclusion']

        p = 'Your Full Body Stats are these:' + \
            '\n' + 'BodyMassIndex (BMI): ' + str(bmi) + 'Kg/m2' + \
            '\n' + 'weight status: ' + str(bmicon) + \
            '\n' + 'BodyFatPercentage: ' + str(bfp) + '%' + \
            '\n' + 'BodyFatPercentage status: ' + str(bfpcon) + \
            '\n' + 'LeanBodyMass: ' + str(lbm) + \
            '\n' + 'Resting Daily Energy Expense: ' + str(rdeec) + 'Kcal' + \
            '\n' + 'Ideal Weight: ' + str(ibw) + 'Kg' + \
            '\n' + 'Waist To Hip Ratio: ' + str(wthr) + \
            '\n' + 'Your Health stat is: ' + str(wthrcon)

        print(p)
    while n:
        try:
            n = int(input('\nDo You want to start again ?\n1- Yes\n2- No\n'))
        except ValueError:
            print('ERROR!!!\nChoose between 1 or 2')
        if 1 <= d <= 2:
            break
        else:
            print('ERROR!!!\nChoose an option: ')
def test():
    print('salam')
