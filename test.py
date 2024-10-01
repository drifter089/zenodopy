import zenodopy

# always start by creating a Client object
zeno = zenodopy.Client(sandbox=True, token="CNXNk6GBg0dQUvZJsCUEajG4ZZnAr8YUrWPR9oCucnu8vq39jFJDUGoYW6WK"
)

# zeno.list_projects

# zeno.create_project(
#     title="twoversionci",
#     upload_type="other",
#     metadata_json=".zenodo.json",
# )
zeno.set_project(dep_id=106299)


# upload file to zenodo
# zeno.upload_file("test.file.txt", publish=True)

# zeno.update(
#     source="/home/akshat/PyPSA/README.md",
#     publish=True,
#     metadata_json=".zenodo.json",
# # )

zeno.rollback_retry(
    dep_id=106299,
    source="/home/akshat/PyPSA/README.md",
    publish=True,
    metadata_json=".zenodo.json",
)

# zeno._delete_project(dep_id=106299)
# zeno.list_files()
# zeno.upload_file("test.file.txt",publish=True)


# zeno.change_metadata(title="my test file",
#                         upload_type="text",
#                         description="Eu reprehenderit non et mollit excepteur nisi laborum labore sit ex ipsum ullamco id. Aute qui fugiat in aute. In quis aute enim cupidatat laborum qui voluptate anim Lorem nulla sint do.",
#                         creator="akshat")
# list project id's associated to zenodo account
