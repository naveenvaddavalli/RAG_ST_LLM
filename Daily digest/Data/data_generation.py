import random
import pandas as pd
from faker import Faker
fake = Faker()

medical_condition_data = {
 'Hypertension': {
 'medications': ['Lisinopril', 'Amlodipine', 'Losartan', 'Hydrochlorothiazide'],
 'cholesterol_range': (100, 200),
 'glucose_range': (70, 110),
 'blood_pressure_range': (140, 90) # systolic/diastolic
 },
 'Diabetes': {
 'medications': ['Metformin', 'Insulin', 'Glipizide', 'Sitagliptin'],
 'cholesterol_range': (100, 200),
 'glucose_range': (130, 200),
 'blood_pressure_range': (130, 80)
 },
 
}
def generate_patient_records(num_patients):
   patient_records = []
   for _ in range(num_patients):
      patient_id = fake.uuid4()
      name = fake.name()
      age = random.randint(18, 90)
      gender = random.choice(['Male', 'Female'])
      blood_type = random.choice(['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-'])
      medical_condition = random.choice(list(medical_condition_data.keys()))
      patient_records.append({
      'Patient_ID': patient_id,
      'Name': name,
      'Age': age,
      'Gender': gender,
      'Blood_Type': blood_type,
      'Medical_Condition': medical_condition
      })
   return patient_records


def generate_test_results(num_patients):
   test_results = []
   for i in range(num_patients):
      patient_id = fake.uuid4()
      medical_condition = random.choice(list(medical_condition_data.keys()))
      cholesterol_range = medical_condition_data[medical_condition]['cholesterol_range']
      glucose_range = medical_condition_data[medical_condition]['glucose_range']
      blood_pressure_range = medical_condition_data[medical_condition]['blood_pressure_range']
      cholesterol = random.uniform(cholesterol_range[0], cholesterol_range[1])
      glucose = random.uniform(glucose_range[0], glucose_range[1])
      systolic = random.randint(blood_pressure_range[1], blood_pressure_range[0]) 
      diastolic = random.randint(60, systolic) 
      blood_pressure = f"{systolic}/{diastolic}"
      test_results.append({
      'Patient_ID': patient_id,
      'Medical_Condition': medical_condition,
      'Cholesterol': cholesterol,
      'Glucose': glucose,
      'Blood_Pressure': blood_pressure
      })
   return test_results

def generate_prescriptions(num_patients):
   prescriptions = []
   for i in range(num_patients):
      patient_id = fake.uuid4()
      medical_condition = random.choice(list(medical_condition_data.keys()))
      medication = random.choice(medical_condition_data[medical_condition]['medications'])
      dosage = f"{random.randint(1, 3)} pills"
      duration = f"{random.randint(1, 30)} days"
      prescriptions.append({
      'Patient_ID': patient_id,
      'Medical_Condition': medical_condition,
      'Medication': medication,
      'Dosage': dosage,
      'Duration': duration
      })
   return prescriptions

def generate_medical_history_dataset(num_patients):
   patient_records = generate_patient_records(num_patients)
   test_results = generate_test_results(num_patients)
   prescriptions = generate_prescriptions(num_patients)
   
   medical_history = []
   for i in range(num_patients):
      patient_id = patient_records[i]['Patient_ID']
      record = {**patient_records[i], **test_results[i], **prescriptions[i]}
      medical_history.append(record)
   return pd.DataFrame(medical_history)

medical_history_dataset = generate_medical_history_dataset(100)

medical_history_dataset.to_csv('medical_history_dataset.csv', index=False)
print("Synthetic medical history dataset created and saved to 'medical_history_dataset.csv'")

