from customtkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from tkinter import StringVar
import tkinter.messagebox as messagebox
import re

# Initialize the main application window
app = CTk()
app.geometry("856x645")
app.resizable(0, 0)

set_appearance_mode("light")

# Sidebar setup
sidebar_frame = CTkFrame(master=app, fg_color="blue", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("flogo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(100, 95))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")


# getting data from the people_count_log.txt
def process_data_from_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Regex to match the line format and extract the datetime and down count
            match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}):\d{2} - Up: (\d+), Down: (\d+)', line)
            if match:
                # Convert string to datetime object, capturing up to minutes for granularity
                timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
                down_count = int(match.group(3))  # Extract down count as integer
                # If this timestamp is not yet in the dictionary, set it to 0
                if timestamp not in data:
                    data[timestamp] = 0
                # down counts by adding them up for each timestamp
                data[timestamp] += down_count
    return data



# Main view setup
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

# Title frame
title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
CTkLabel(master=title_frame, text="Occupancy Counter", font=("Arial Black", 25), text_color="red").pack(anchor="nw", side="left")

# put the name of the building name for occupancy count
search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(45, 0), padx=27)

store_name_var = StringVar()  # Variable to hold the store name
time_range_var = StringVar()  # Variable to hold the selected time range

# Reset graph view to show the full graph 
def reset_graph_view():
    global people_count_data  
    people_count_data = process_data_from_file('people_count_log.txt')  # Process data
    x, y = list(people_count_data.keys()), list(people_count_data.values())
    ax.clear()
    ax.plot(x, y, color="blue")
    ax.set_xlim([min(x), max(x)])  # Adjust this if you want to set specific start and end times

    # Set the y-axis (people count) to have a fixed limit from 0 to 500
    ax.set_ylim([0, 500])

    # Format the x-axis to display times
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))

    # Rotate the x-axis labels for readability
    plt.xticks(rotation=45)

    # Adjust subplot parameters to give the x-axis labels room
    plt.subplots_adjust(bottom=0.2)

    # Redraw the canvas with the new plot
    canvas.draw()


# Function to update the graph title
def update_graph_title(*args):
    store_name = store_name_var.get()
    if store_name:
        ax.set_title(f"Occupancy for {store_name}", fontsize =20)  # Set the new title for the graph
        canvas.draw()


# select time range option button

def update_graph_data(selected_time_range):
    # Directly fetching the store name from store_name_var within the function
    store_name = store_name_var.get().strip() or "The selected store"
    
    # Use the current date 
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Parse the selected_time_range to create a datetime object that matches your data keys
    # The time range format in the ComboBox is assumed to be like "12:00 A.M - 1:00 A.M"
    start_time_str = current_date_str + " " + selected_time_range.split(" - ")[0]
    
    # Adjust the datetime format to match the keys in your data
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %I:%M %p")
    
    # Use the start_time datetime object to get the count of people
    # Assuming people_count_data is a dictionary where keys are datetime objects
    people_count = people_count_data.get(start_time, 0)  # Default to 0 if not found
    
    ax.clear()
    
    x = [start_time]  # X-axis is datetime objects for bar plot
    y = [people_count]  # Y-axis is a list of the people count
    
    # Generate a bar plot with the selected time range and the count of people
    ax.bar(x, y, width=0.02, color="blue")  # Adjust width as needed for visibility
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.set_ylim(0, max(y) + 500)  # Adjust the y-axis limit to make the bar visible
    
    # Adjust x-axis limits to focus on the selected time range
    ax.set_xlim(start_time, start_time + timedelta(hours=1))
    
    # Set labels and title
    ax.set_ylabel('Number of People', fontsize=12)
    ax.set_title(f'Number of People in {store_name} for {selected_time_range}: {people_count}', fontsize=13)
    
    # Redraw the canvas with the new plot
    canvas.draw()


#find buisest people

def find_busiest_period(data):
    # Find the key (time) with the maximum people count
    busiest_time = max(data, key=data.get)
    busiest_count = data[busiest_time]
    
    # Format the busiest_time as a string
    busiest_time_str = busiest_time.strftime("%I:%M %p")
    
    return busiest_time_str, busiest_count


def display_busiest_period():
    busiest_time_str, busiest_count = find_busiest_period(people_count_data)
    
    # Convert busiest_time_str to a datetime object
    busiest_time = datetime.strptime(busiest_time_str, "%I:%M %p")
    
    # Calculate the end time, which is one hour later
    end_time = busiest_time + timedelta(hours=1)
    
    # Format the start and end times as strings in the desired format
    busiest_time_str = busiest_time.strftime("%I:%M %p")
    end_time_str = end_time.strftime("%I:%M %p")
    
    # Create the time range string
    time_range_str = f"{busiest_time_str} - {end_time_str}"
    
    message = f"The time when the most people are present is {time_range_str} with {busiest_count} people."
    messagebox.showinfo("Most people occupancy time range", message)

# Find least people

def find_least_period(data):

    # Find the key (time) with the minimum people count
    least_time = min(data, key=data.get)
    least_count = data[least_time]
    
    # Format the least_time as a string
    least_time_str = least_time.strftime("%I:%M %p")
    
    return least_time_str, least_count

def display_least_period():
    least_time_str, least_count = find_least_period(people_count_data)
    
    least_time = datetime.strptime(least_time_str, "%I:%M %p")
    
    end_time = least_time + timedelta(hours=1)
    
    least_time_str = least_time.strftime("%I:%M %p")
    end_time_str = end_time.strftime("%I:%M %p")
    
    time_range_str = f"{least_time_str} - {end_time_str}"
    
    message = f"The time when the least people are present is {time_range_str} with {least_count} people."
    messagebox.showinfo("least people occupancy time range", message)


# Entry for the store name
store_name_entry = CTkEntry(master=search_container, textvariable=store_name_var, width=305, placeholder_text="Put your Store name", border_color="red", border_width=2)
store_name_entry.pack(side="left", padx=(13, 0), pady=15)

store_name_var.trace_add("write", update_graph_title)  # Update the graph title when the store name is entered

# Create a frame for the buttons
button_frame = CTkFrame(master=main_view)
button_frame.pack(pady=10)  # Adjust padding as necessary

busiest_button = CTkButton(master=button_frame, text="Peak occupancy time", command=display_busiest_period, fg_color="red", hover_color="#207244")
busiest_button.pack(side='left', padx=10)  

least_button = CTkButton(master=button_frame, text="Least occupancy time", command=display_least_period, fg_color="red", hover_color="#207244")
least_button.pack(side='left', padx=10)

go_back_button = CTkButton(master=button_frame, text="Go Back to Full Graph", command=reset_graph_view, fg_color="red", hover_color="#207244")
go_back_button.pack(side='left', padx=10)


time_range_combobox = CTkComboBox(master=search_container, width=180, values=["Select Time Range ", "12:00 AM - 1:00 AM ", "1:00 AM - 2:00 AM", "2:00 AM - 3:00 AM", "3:00 AM - 4:00 AM","4:00 AM - 5:00 AM","5:00 AM - 6:00 AM","6:00 AM - 7:00 AM","7:00 AM - 8:00 AM","8:00 AM - 9:00 AM","9:00 AM - 10:00 AM","10:00 AM - 11:00 AM","11:00 AM - 12:00 PM","12:00 PM - 1:00 PM","1:00 PM - 2:00 PM","2:00 PM - 3:00 PM","3:00 PM - 4:00 PM","4:00 PM - 5:00 PM","5:00 PM - 6:00 PM","6:00 PM - 7:00 PM","7:00 PM - 8:00 PM","8:00 PM - 9:00 PM","9:00 PM - 10:00 PM","10:00 PM - 11:00 PM","11:00 PM - 12:00 AM"], button_color="red", border_color="red", border_width=2, button_hover_color="#207244", dropdown_hover_color="#207244", dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
time_range_combobox.pack(side="left", padx=(13, 0), pady=15)
time_range_combobox.set("Select time range") 


# Bind the callback function to the combobox
time_range_combobox.configure(command=update_graph_data)

# Prepare time data (x) and people count data (y)
start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
end_time = start_time + timedelta(hours=23, minutes=59)  # Set end time to just before midnight
x = [start_time + timedelta(hours=i) for i in range(24)]  # Generate a datetime object for each hour
y = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]  

# Create the figure and axes for the graph
fig, ax = plt.subplots(figsize=(10, 4))

# Set the formatter and locator for the x-axis
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))  

ax.set_xlim(start_time, end_time)  # Set the limits of the x-axis to only show the current day

plt.xticks(rotation=45)  # Rotate the x-axis labels for readability
plt.subplots_adjust(bottom=0.2)  # Adjust subplot to make room for the x-axis labels

# Embed the plot into the Tkinter GUI
canvas = FigureCanvasTkAgg(fig, master=main_view)
canvas.draw()

# Display the canvas
canvas.get_tk_widget().pack(expand=True, fill='both')

# Start the Tkinter event loop
if __name__ == "__main__":
    reset_graph_view()  
    app.mainloop() 
