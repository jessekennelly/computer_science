popular_s_names = [
    "Sabrina",
    "Sadie",
    "Sage",
    "Saige",
    "Saint",
    "Salem",
    "Samantha",
    "Samara",
    "Samuel",
    "Santiago",
    "Santino",
    "Sara",
    "Sarah",
    "Sarai",
    "Sasha",
    "Saul",
    "Savannah",
    "Sawyer",
    "Saylor",
    "Scarlet",
    "Scarlett",
    "Sean",
    "Sebastian",
    "Selah",
    "Selena",
    "Serena",
    "Serenity",
    "Sergio",
    "Seth",
    "Shane",
    "Shawn",
    "Shelby",
    "Shepherd",
    "Shiloh",
    "Sienna",
    "Sierra",
    "Silas",
    "Simon",
    "Skye",
    "Skylar",
    "Skyler",
    "Sloan",
    "Sloane",
    "Sofia",
    "Solomon",
    "Sonny",
    "Sophia",
    "Sophie",
    "Soren",
    "Spencer",
    "Stella",
    "Stephanie",
    "Stephen",
    "Sterling",
    "Stetson",
    "Steven",
    "Stevie",
    "Sullivan",
    "Summer",
    "Sutton",
    "Sydney",
    "Sylas",
    "Sylvia",
    "Sylvie",
]
x = 0
y = 0
long_s_names = []
for i in range(len(popular_s_names)):
    if len(popular_s_names[i]) < 5:
        x+=1
    elif len(popular_s_names[i]) >= 8:
        long_s_names.append(popular_s_names[i])
    else:
        y+=1
print(x)
print(y)
print(long_s_names)