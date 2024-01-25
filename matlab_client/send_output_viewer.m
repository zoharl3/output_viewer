
function send_output_viewer(txt)
% For garbage collection error see
% https://au.mathworks.com/matlabcentral/answers/100335-why-do-i-receive-an-error-when-i-execute-the-fetch-statement-on-a-sql-server-database-using-database

if 0
    data = char(strcat('|', txt));
    
    %global output_viewer_tcp;
    %persistent output_viewer_tcp;
    output_viewer_tcp = [];

    try
        if isempty( output_viewer_tcp )
            % test with
            %   echotcpip( 'on', 32313 )
            %   echotcpip( 'off' )
            % https://au.mathworks.com/matlabcentral/answers/1578545-tcpclient-slow-connection

            %output_viewer_tcp = tcpclient( '127.0.0.1', 32313, 'Timeout', 1, 'ConnectTimeout', 5 ); % slow
            output_viewer_tcp = tcpclient( '127.0.0.1', 32313 );
        end
        write( output_viewer_tcp, uint8(data) );
        flush( output_viewer_tcp );
    catch ex
        disp(['send_output_viewer() error: ' ex.message]);
        delete( output_viewer_tcp );
        output_viewer_tcp = [];
        clear output_viewer_tcp;
    end

    if 1
        delete( output_viewer_tcp );
        output_viewer_tcp = [];
        clear output_viewer_tcp;
    end
    
else % logger
    log = clib.send_output_viewer.OutputViewer;
    log.print( txt );
end

