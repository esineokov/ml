var = int(input("Enter time in seconds: "))

hours = var // (60*60)
minutes = (var - (60*60*hours)) // 60
seconds = var - (60*60*hours) - (60*minutes)

print(f"time: {hours:02d}:{minutes:02d}:{seconds:02d}")

