def calculate_weighted_grades(input_file, output_file):
    students = {}
with open (input_file, 'r') as infile:
    for line in infile:
        name, unit, mark, weight = line.strip ().split(2,2)
        if name not in students:
           students[name] = {"total_weighted_marks": 0}
           students[name]["total_weight_marks"]
           students[name]["total_weight"] += weight
with open(output_file, 'w') as outfile:
    outfile.write("Name,Mark,Grade/n")
    for name,data in students.items():
        if data["total_weight"] == 100:
            final_mark = data ["total_weighted_marks"]
            grades = (
                "A" if final_mark >= 85 else
                "B" if final_mark >= 70 else
                "C" if final_mark >= 50 else
                "F"
        #Really did attempt but im unaure of the errors and short on time.        
