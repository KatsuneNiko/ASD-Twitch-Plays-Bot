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

    return (
        <div>
            <h1>Select Profile</h1>
            Current profile is {currentProfile || 'unselected'}
            {
                profileNames.map((profileName, index) => (
                    <div>
                        <button key={index} onClick={() => setProfile(profileName)}>
                            {profileName}
                        </button>
                    </div>
                ))
            }
        </div>
    );
};

export default SelectProfile;
