# Choregraphe simplified export in Python.
def MoveFive():
    names = list()
    times = list()
    keys = list()
    
    names.append("HeadPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.274628, -0.345192, -0.300706, -0.274628, -0.345191, -0.300706, -0.274628, -0.345191, -0.300706, -0.274628, -0.345191, -0.300706, -0.274628, -0.345191, -0.300706, -0.274628, -0.345191, -0.300706])
    
    names.append("HeadYaw")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.14117, -0.128898, -0.119694, -0.14117, -0.128898, -0.119694, -0.14117, -0.128898, -0.119694, -0.14117, -0.128898, -0.119694, -0.14117, -0.128898, -0.119694, -0.14117, -0.128898, -0.119694])
    
    names.append("LAnklePitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.0843279, 0.00455999, -0.016916, 0.0843279, 0.00455999, -0.016916, 0.0843279, 0.00455999, -0.016916, 0.0843279, 0.00455999, -0.016916, 0.0843279, 0.00455999, -0.016916, 0.0843279, 0.00455999, -0.016916])
    
    names.append("LAnkleRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.130348, -0.124212, -0.0919981, -0.130348, -0.124212, -0.091998, -0.130348, -0.124212, -0.091998, -0.130348, -0.124212, -0.091998, -0.130348, -0.124212, -0.091998, -0.130348, -0.124212, -0.091998])
    
    names.append("LElbowRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-1.54462, -1.52015, -1.51095, -1.54462, -1.52015, -1.51095, -1.54462, -1.52015, -1.51095, -1.54462, -1.52015, -1.51095, -1.54462, -1.52015, -1.51095, -1.54462, -1.52015, -1.51095])
    
    names.append("LElbowYaw")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.994074, -0.994074, -0.981802, -0.994073, -0.994073, -0.981802, -0.994073, -0.994073, -0.981802, -0.994073, -0.994073, -0.981802, -0.994073, -0.994073, -0.981802, -0.994073, -0.994073, -0.981802])
    
    names.append("LHand")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.2912, 0.2912, 0.2884, 0.2912, 0.2912, 0.2884, 0.2912, 0.2912, 0.2884, 0.2912, 0.2912, 0.2884, 0.2912, 0.2912, 0.2884, 0.2912, 0.2912, 0.2884])
    
    names.append("LHipPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.130432, -0.11961, -0.358914, 0.130432, -0.11961, -0.358915, 0.130432, -0.11961, -0.358915, 0.130432, -0.11961, -0.358915, 0.130432, -0.11961, -0.358915, 0.130432, -0.11961, -0.358915])
    
    names.append("LHipRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.096684, 0.112024, 0.130432, 0.0966839, 0.112024, 0.130432, 0.0966839, 0.112024, 0.130432, 0.0966839, 0.112024, 0.130432, 0.0966839, 0.112024, 0.130432, 0.0966839, 0.112024, 0.130432])
    
    names.append("LHipYawPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.167164, -0.245398, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728])
    
    names.append("LKneePitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.0890141, 0.228524, 0.490838, -0.0890141, 0.228525, 0.490837, -0.0890141, 0.228525, 0.490837, -0.0890141, 0.228525, 0.490837, -0.0890141, 0.228525, 0.490837, -0.0890141, 0.228525, 0.490837])
    
    names.append("LShoulderPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.28068, 0.314428, 0.352778, 0.28068, 0.314428, 0.352778, 0.28068, 0.314428, 0.352778, 0.28068, 0.314428, 0.352778, 0.28068, 0.314428, 0.352778, 0.28068, 0.314428, 0.352778])
    
    names.append("LShoulderRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.306842, -0.270026, -0.247016, -0.306841, -0.270025, -0.247016, -0.306841, -0.270025, -0.247016, -0.306841, -0.270025, -0.247016, -0.306841, -0.270025, -0.247016, -0.306841, -0.270025, -0.247016])
    
    names.append("LWristYaw")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.41107, 0.41107, 0.401866, 0.41107, 0.41107, 0.401866, 0.41107, 0.41107, 0.401866, 0.41107, 0.41107, 0.401866, 0.41107, 0.41107, 0.401866, 0.41107, 0.41107, 0.401866])
    
    names.append("RAnklePitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.090548, -0.056716, -0.118076, 0.090548, -0.056716, -0.118076, 0.090548, -0.056716, -0.118076, 0.090548, -0.056716, -0.118076, 0.090548, -0.056716, -0.118076, 0.090548, -0.056716, -0.118076])
    
    names.append("RAnkleRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.136568, 0.12583, 0.142704, 0.136568, 0.12583, 0.142704, 0.136568, 0.12583, 0.142704, 0.136568, 0.12583, 0.142704, 0.136568, 0.12583, 0.142704, 0.136568, 0.12583, 0.142704])
    
    names.append("RElbowRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.661196, 0.529272, 0.43263, 0.661195, 0.529273, 0.43263, 0.661195, 0.529273, 0.43263, 0.661195, 0.529273, 0.43263, 0.661195, 0.529273, 0.43263, 0.661195, 0.529273, 0.43263])
    
    names.append("RElbowYaw")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([1.22102, 1.06455, 1.03081, 1.22102, 1.06455, 1.03081, 1.22102, 1.06455, 1.03081, 1.22102, 1.06455, 1.03081, 1.22102, 1.06455, 1.03081, 1.22102, 1.06455, 1.03081])
    
    names.append("RHand")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.2916, 0.2916, 0.288, 0.2916, 0.2916, 0.288, 0.2916, 0.2916, 0.288, 0.2916, 0.2916, 0.288, 0.2916, 0.2916, 0.288, 0.2916, 0.2916, 0.288])
    
    names.append("RHipPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([0.12728, -0.105888, -0.343658, 0.12728, -0.105888, -0.343659, 0.12728, -0.105888, -0.343659, 0.12728, -0.105888, -0.343659, 0.12728, -0.105888, -0.343659, 0.12728, -0.105888, -0.343659])
    
    names.append("RHipRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.102736, -0.0966001, -0.0950661, -0.102736, -0.0966001, -0.095066, -0.102736, -0.0966001, -0.095066, -0.102736, -0.0966001, -0.095066, -0.102736, -0.0966001, -0.095066, -0.102736, -0.0966001, -0.095066])
    
    names.append("RHipYawPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.167164, -0.245398, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728, -0.167164, -0.245399, -0.237728])
    
    names.append("RKneePitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.0919981, 0.259288, 0.492456, -0.091998, 0.259288, 0.492455, -0.091998, 0.259288, 0.492455, -0.091998, 0.259288, 0.492455, -0.091998, 0.259288, 0.492455, -0.091998, 0.259288, 0.492455])
    
    names.append("RShoulderPitch")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-1.175, -0.4801, 0.0123138, -1.175, -0.4801, 0.0123138, -1.175, -0.4801, 0.0123138, -1.175, -0.4801, 0.0123138, -1.175, -0.4801, 0.0123138, -1.175, -0.4801, 0.0123138])
    
    names.append("RShoulderRoll")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.289968, -0.0629361, -0.04913, -0.289967, -0.062936, -0.04913, -0.289967, -0.062936, -0.04913, -0.289967, -0.062936, -0.04913, -0.289967, -0.062936, -0.04913, -0.289967, -0.062936, -0.04913])
    
    names.append("RWristYaw")
    times.append([1.2, 1.8, 2.4, 3.6, 4.2, 4.8, 6, 6.6, 7.2, 8.4, 9, 9.6, 10.8, 11.4, 12, 13.2, 13.8, 14.4])
    keys.append([-0.917374, -0.948054, -0.94652, -0.917375, -0.948054, -0.94652, -0.917375, -0.948054, -0.94652, -0.917375, -0.948054, -0.94652, -0.917375, -0.948054, -0.94652, -0.917375, -0.948054, -0.94652])
    
    return names, keys, times
    