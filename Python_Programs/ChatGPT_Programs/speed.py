import speedtest

# Create an object of the Speedtest class
st = speedtest.Speedtest()

# Get the ping (latency) of the internet connection
ping = st.get_servers()[0]["latency"]

# Get the download speed in megabits per second (Mbps)
download_speed = st.download() / 1000000

# Get the upload speed in megabits per second (Mbps)
upload_speed = st.upload() / 1000000

# Print the ping, download speed, and upload speed
print(f"Ping: {ping:.2f} ms")
print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
