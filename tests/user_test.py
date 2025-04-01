import pytest
from unittest.mock import AsyncMock, MagicMock, patch, Mock
from the_network_backend.db.lib import userlib

@pytest.mark.asyncio
@patch('the_network_backend.db.lib.userlib.SessionLocal', new_callable=MagicMock)
@patch('the_network_backend.db.lib.userlib.hash_password', new_callable=AsyncMock)
async def test_create_user(mock_hash_password, mock_session):
    # Arrange
    username = "testuser"
    password = "testpassword"
    email = "testuser@example.com"
    hashed_password = "hashedpassword"
    
    mock_hash_password.return_value = hashed_password
    mock_session_instance = AsyncMock()
    mock_session_instance.commit = AsyncMock()
    mock_session_instance.refresh = AsyncMock()
    mock_session_instance.add = Mock()
    mock_session.return_value.__aenter__.return_value = mock_session_instance

    # Act
    user = await userlib.create_user(username, password, email)

    # Assert
    assert user.username == username
    assert user.password == hashed_password
    assert user.email == email
    mock_session_instance.add.assert_called_once_with(user)
    mock_session_instance.commit.assert_awaited_once()
    mock_session_instance.refresh.assert_awaited_once_with(user)