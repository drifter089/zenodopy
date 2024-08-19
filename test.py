import zenodopy

# always start by creating a Client object
zeno = zenodopy.Client(sandbox=True)

# zeno.list_projects

zeno.create_project(title="twoversion10", upload_type="other")


# upload file to zenodo
zeno.upload_file("test.file.txt", publish=True)
zeno.update(source="/home/akshat/zenodopy", publish=True)
# zeno.list_files()
# zeno.upload_file("test.file.txt",publish=True)


# zeno.change_metadata(title="my test file",
#                         upload_type="text",
#                         description="Eu reprehenderit non et mollit excepteur nisi laborum labore sit ex ipsum ullamco id. Aute qui fugiat in aute. In quis aute enim cupidatat laborum qui voluptate anim Lorem nulla sint do.",
#                         creator="akshat")
# list project id's associated to zenodo account
