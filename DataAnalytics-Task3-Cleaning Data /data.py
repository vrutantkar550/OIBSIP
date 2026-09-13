import kagglehub

# Download latest version
path = kagglehub.dataset_download("maxhorowitz/nflplaybyplay2009to2016")

print("NFL Play by Play 2009-2016 (v3).csv", path)
