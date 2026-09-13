try:
	import urllib3 
except ImportError as e:
	print("\n\n".join("Import Error(s)".center(80,'=')))
	print(f"Package {e.name} is required for this tool!")

def hostsToDomainList(targetUrl):
	http = urllib3.PoolManager()
	response = http.request("GET", targetUrl)
	data = response.data.decode("ascii")

	output = ""
	for line in data.split("\n"):
		if (
		(line is not None) 
		and (line != "") 
		and (line[0] != "#")
		and (line[:8] == "0.0.0.0 ")
		):
			cleanLine = line.replace("0.0.0.0", "").strip()
			if (cleanLine != ""):
				output += cleanLine + "\n"
	return output