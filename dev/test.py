import peddesign
import pkg_resources
import site

# peddesign.design_ct("chest", 10)


print(site.getsitepackages())

def get_package_path(package_name):
    try:
        package = pkg_resources.get_distribution(package_name)
        return package.location
    except pkg_resources.DistributionNotFound:
        return f"Package '{package_name}' not found"

# Replace 'testPKG' with the name of the package you're interested in
# print(get_package_path("customtkinter"))


