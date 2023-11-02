import React, { useEffect, useState } from "react";

const SelectProfile = () =>  {
    const [profileNames, setProfileNames] = useState([]);
    const [currentProfile, setCurrentProfile] = useState(null);

    useEffect(() => {
        (async () => {
            const request = await fetch('/ProfileManager');
            const requestJson = await request.json();
            setProfileNames(requestJson.profileNames);
            setCurrentProfile(requestJson.currentProfile);
        })()
    }, []);

    const setProfile = async (profileName) => {
        const request = await fetch('/ProfileManager', {
            method: 'POST',
            body: JSON.stringify({ 
                method: 'select',
                name: profileName
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const requestJson = await request.json();
        setProfileNames(requestJson.profileNames);
        setCurrentProfile(requestJson.currentProfile);
    }

    const createProfile = async (profileName) => {
        const request = await fetch('/ProfileManager', {
            method: 'POST',
            body: JSON.stringify({ 
                method: 'create',
                name: profileName
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const requestJson = await request.json();
        setProfileNames(requestJson.profileNames);
        setCurrentProfile(requestJson.currentProfile);
    }

    const deleteProfile = async (profileName) => {
        const request = await fetch('/ProfileManager', {
            method: 'POST',
            body: JSON.stringify({ 
                method: 'delete',
                name: profileName
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const requestJson = await request.json();
        setProfileNames(requestJson.profileNames);
        setCurrentProfile(requestJson.currentProfile);
    }

    return (
        <div>
            <h1>Profile Manager</h1>
            <div>
                <h2>Select Profile</h2>
                Current profile is {currentProfile || 'unselected'}
                <table>
                {
                    profileNames.map((profileName, index) => (
                        <tr key={index}>
                            <td>
                                {profileName}
                            </td>
                            <td>
                                <button onClick={() => setProfile(profileName)}>
                                    Select
                                </button>
                                <button onClick={() => deleteProfile(profileName)}>
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))
                }
                </table>
            </div>
            <div>
                <h2>Create Profile</h2>
                <form onSubmit={(event) => {
                    event.preventDefault();
                    createProfile(event.target.profileName.value);
                }}>
                    <input name="profileName" type="text" />
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    );
};

export default SelectProfile;
