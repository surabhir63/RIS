import numpy as np
import subprocess
import os
import shutil  

#"C:\Program Files\Remcom\Wireless InSite 3.4.4\bin\calc\wibatch.exe" -f "C:\Users\scsdc\senior_design\Without_EES_bak\Rev2\Simple_EES.WithEES.xml" -out "C:\Users\scsdc\senior_design\Without_EES_bak\study area" -set_licenses 27000@Insite-Desktop

# File paths 
wibatch_exe = r"C:\Program Files\Remcom\Wireless InSite 3.4.4\bin\calc\wibatch.exe" #Path to execute wireless insite
ees_file = r"C:\Users\scsdc\senior_design\Call\EES_Plate.ees" #The original EES file that needs to be modified
output_folder = r"C:\Users\scsdc\senior_design\Without_EES_bak\study area" #directory where Wireless insite stores output
results_directory = r"C:\Users\scsdc\senior_design\Simulation_Results" #directory where all the extracted simulation results will be added
modified_ees_folder = r"C:\Users\scsdc\senior_design\Modified_EES_Files" #directory to save all the modified EES files
xml_project_file = r"C:\Users\scsdc\senior_design\Call\CallTest.Full Study Area_EES.xml" #Path to XML project file. the simulation model??

# Ensure required directories exist
os.makedirs(results_directory, exist_ok=True)
os.makedirs(modified_ees_folder, exist_ok=True)

# Define sine values from sin(170°) to sin(175°) in steps of 5° (need to change to -175 to 175 once everything is verified)
sine_angles = np.arange(22, 171, 1)  # Degrees
sine_values = np.sin(np.radians(sine_angles))  # Convert to sin(x)


def modify_rows(file_path, sin_value, angle):
    """Update all rows in <data> section with the same sine value and save a copy of the modified EES file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_data_section = False
    in_row_section = False
    modified_lines = []

    for line in lines:
        if "begin_<data>" in line:
            in_data_section = True
        elif "end_<data>" in line:
            in_data_section = False

        if in_data_section and "begin_<row>" in line:
            in_row_section = True
        elif in_data_section and "end_<row>" in line:
            in_row_section = False

        if in_row_section and not ("begin_<row>" in line or "end_<row>" in line):
            parts = line.strip().split()
            if parts:
                parts[0] = f"{sin_value:.15f}"  # Store sin(x) value 
                modified_lines.append(" ".join(parts) + "\n")
                continue

        modified_lines.append(line)  # Keep all other lines unchanged

    # Overwrite the original EES file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

    print(f"Updated '{file_path}' with sin({angle}°) = {sin_value:.15f}")

    # Save a copy of the modified EES file
    reference_filename = os.path.join(modified_ees_folder, f"EES_sin_{angle}.ees")
    with open(reference_filename, 'w') as ref_file:
        ref_file.writelines(modified_lines)

    print(f"Saved reference EES file: {reference_filename}")

    return file_path  # Return the modified file path


def run_wireless_insite(xml_file, output_dir):
    """Run Wireless InSite simulation using command line."""
    print(f"Running Wireless InSite simulation for {xml_file}...")

    process = subprocess.Popen(
        [wibatch_exe, "-f", xml_file, "-out", output_dir, "-set_licenses", "27000@Insite-Desktop"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"Wireless InSite simulation completed successfully for {xml_file}")
    else:
        print(f"Error in Wireless InSite simulation for {xml_file}:", stderr.decode())


def extract_results(output_folder, angle):

    """Extract all simulation result files and move them to Simulation_Results."""
    output_files = os.listdir(output_folder)
    if not output_files:
        print(f"Error: No simulation results found for angle {angle}°.")
        return

    # Move and rename all output files for each sin(x) values
    for filename in output_files:
        old_path = os.path.join(output_folder, filename)

        if not os.path.isfile(old_path):
            print(f"Skipping non-file item: {old_path}")
            continue

        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}_sin_{angle}{extension}"
        new_path = os.path.join(results_directory, new_filename)

        shutil.copy(old_path, new_path) 
        print(f"Copied simulation output: {old_path} → {new_path}")

def clear_output_folder(output_folder):
    """Delete all previous results before running a new simulation."""
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted old result: {file_path}")



# Loop Through All Angles & Run Simulations
for i, sin_value in enumerate(sine_values):
    angle = sine_angles[i]  # Get the correct angle

    # Modify & Overwrite ees_file, also saves a copy aswell
    modified_ees_path = modify_rows(ees_file, sin_value, angle)
    
    # Call this function before running the simulation
    clear_output_folder(output_folder)

    # Run Wireless InSite using the modified EESfile
    run_wireless_insite(xml_project_file, output_folder)

    # Extract and save results inside the new directory for simulation resukts
    extract_results(output_folder, angle)

print("All simulations completed.")
