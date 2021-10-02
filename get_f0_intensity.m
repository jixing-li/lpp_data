% This function returns the f0, RMS intensity of a wav file using Voicebox

function [intensity,f0] = get_f0_intensity(fname)

    [wav,Fs] = audioread(fname);

    % over 10 ms interval, calculate rms intensity
    disp('Calculating RMS intensity...')
    wavb = buffer(wav,round(0.02*Fs),round(0.01*Fs),'nodelay');
    intensity = [0,sqrt(mean(wavb.^2))];
    disp('RMS intensity done.')

    time = 0:0.01:(length(intensity)-1)/100; 
    % pitchtracking using voicebox function fxrapt, default time frame: 10ms
    disp('Extracting f0...')
    [f0,tt] = fxrapt(wav,Fs,'u');

    % take the middle point in the time frame for the f0 value (5, 15, 25 ms...)
    time_f0 = mean(tt(:,1:2),2)/Fs;

    % linear interpolate the time points at the 0, 10, 20 ms ...
    f0 = interp1(time_f0,f0,time,'linear');

    % replace nans with 0
    f0(isnan(f0)) = 0;
    disp('f0 done.')
end


