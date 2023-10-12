import ProfileManager as ProfileManager

def test_createProfile():
    ProfileManager.createProfile("TestProfile")
    assert ProfileManager.profile == "TestProfile"

def test_profileExists():
    assert ProfileManager.profileExists("TestProfile")

def test_deleteProfile():
    ProfileManager.deleteProfile("TestProfile")
    assert ProfileManager.profile == '' and not ProfileManager.profileExists("TestProfile")
