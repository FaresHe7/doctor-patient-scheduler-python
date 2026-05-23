class patient:
    def __init__(self,name ,health_condition,age,booking):
        self.name=name
        self.health_condition= health_condition
        self.age = age
        self.booking=booking
    def patient_info(self):
        return (f"name {self.name} helth {self.health_condition} {self.age} {self.booking}")



class doctor:
    total_patient=0
    working_hours= [8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16]
    def __init__(self,name):
        self.name=name
        self.scheduling=[]
    def book(self,patient):
 
        #working_hours= [8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16]

        if self.total_patient >=16:
            return(f"booking not available for today")
        
        elif patient.booking not in doctor.working_hours:
                return (f"Please choose an appointment time from the following options {doctor.working_hours}")
        
        
        elif patient.booking in self.scheduling:
            return (f"sorry this time booked befor Please choose another time {doctor.working_hours}")
        
        else:
            doctor.total_patient += 1
            self.scheduling.append(patient.booking)
            doctor.working_hours.remove(patient.booking)
            return(f"Booking successful Your appointment is confirmed at {patient.booking} your name is {patient.name}, your age {patient.age}, your Health Condition {patient.health_condition}")






clinic = doctor("clinic Health")

patient_1 = patient("ahmed","stomach ache",20,9.5)
patient_2 = patient("mohamed","stomach ache",18,8.5)
patient_3 = patient("zaki","stomach ache",18,9.5)
patient_4 = patient("messi","stomach ache",18,9)


clinic.book(patient_1)

clinic.book(patient_2)

clinic.book(patient_3)

patient_2.patient_info()