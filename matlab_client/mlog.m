
% example: mlog( 'hi\n' );

function mlog(varargin)
if nargin == 0
    st = '';
else
    st = string( sprintf(varargin{:}) );
end

mlog_st( st );

