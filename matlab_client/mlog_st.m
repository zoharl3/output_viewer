
function mlog_st( st )
%return;

fprintf("%s", st);
%return;

fname = 'mlog.settings';
if 1&& exist(fname, 'file') == 2 % disable to make it faster for the patch optimization?
    fid = fopen(fname);
    mode = fread(fid);
    fclose(fid);
    if mode == '1'
        send_output_viewer(st);
    end
end

if 1
    ldir = '/prj/test_data/relative/_tmp/'; % Zohar

    if exist(ldir, 'file') ~= 7
        return;
    end

    fname = [ldir '_matlab_out.txt'];

    fid = fopen(fname, 'a');
    fprintf(fid, "%s", st);
    fclose(fid);
end

