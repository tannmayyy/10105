import pkg_resources

packages = pkg_resources.working_set
packages_list = ["%s==%s" % (i.key, i.version) for i in packages]

# Save to a .txt file
with open("packages_list.txt", "w") as file:
    for package in packages_list:
        file.write(package + "\n")
