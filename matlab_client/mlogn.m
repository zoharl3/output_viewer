
% example: mlogn( 'hi' );

function mlogn(varargin)
if nargin == 0
    st = '';
else
    st = sprintf(varargin{:});
end

% '\n' isn't the character but a string that needs parsing
mlog_st( [ st newline ] );

